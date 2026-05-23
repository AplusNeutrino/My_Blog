# frozen_string_literal: true

require 'date'
require 'json'
require 'net/http'
require 'uri'

GOATCOUNTER_CODE = ENV.fetch('GOATCOUNTER_CODE', 'neutrinothex')
API_TOKEN = ENV.fetch('GOATCOUNTER_API_TOKEN', '')
POPULAR_DAYS = ENV.fetch('POPULAR_DAYS', '90').to_i
POPULAR_LIMIT = ENV.fetch('POPULAR_LIMIT', '32').to_i
OUTPUT_PATH = ENV.fetch('POPULAR_OUTPUT', '_data/home_popular.yml')

if API_TOKEN.empty?
  warn 'GOATCOUNTER_API_TOKEN is empty; skipping home popular update.'
  exit 0
end

def normalize_post_path(path)
  return nil if path.nil? || path.empty?

  path = URI(path).path if path.match?(%r{\Ahttps?://})
  path = path.split('?').first.split('#').first
  path = "/#{path}" unless path.start_with?('/')
  path = "#{path}/" unless path.end_with?('/')
  return nil unless path.start_with?('/posts/')

  URI::DEFAULT_PARSER.escape(path, /[^A-Za-z0-9\-._~\/%]/)
end

def extract_path_counts(value, results = [])
  case value
  when Array
    value.each { |entry| extract_path_counts(entry, results) }
  when Hash
    path = value['path'] || value['pathname'] || value['url'] || value['name']
    count = value['count'] || value['hits'] || value['pageviews'] || value['views'] || value['total']

    results << [path, count.to_i] if path.is_a?(String)
    value.each_value { |entry| extract_path_counts(entry, results) }
  end

  results
end

def fetch_goatcounter_hits
  end_date = Date.today
  start_date = end_date - POPULAR_DAYS
  uri = URI("https://#{GOATCOUNTER_CODE}.goatcounter.com/api/v0/stats/hits")
  uri.query = URI.encode_www_form(
    start: start_date.iso8601,
    end: end_date.iso8601,
    limit: 200
  )

  request = Net::HTTP::Get.new(uri)
  request['Authorization'] = "Bearer #{API_TOKEN}"
  request['Accept'] = 'application/json'

  response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
    http.request(request)
  end

  unless response.is_a?(Net::HTTPSuccess)
    abort "GoatCounter API request failed: HTTP #{response.code} #{response.body}"
  end

  JSON.parse(response.body)
end

data = fetch_goatcounter_hits
ranked_paths = extract_path_counts(data)
  .filter_map { |path, count| normalized = normalize_post_path(path); [normalized, count] if normalized }
  .group_by(&:first)
  .map { |path, entries| [path, entries.sum { |entry| entry[1] }] }
  .sort_by { |path, count| [-count, path] }
  .map(&:first)
  .first(POPULAR_LIMIT)

content = +"# Generated from GoatCounter path stats. Do not store public view counts here.\n\nposts:\n"
ranked_paths.each do |path|
  content << "  - #{path}\n"
end

File.write(OUTPUT_PATH, content)
puts "Wrote #{ranked_paths.size} popular post path(s) to #{OUTPUT_PATH}."
