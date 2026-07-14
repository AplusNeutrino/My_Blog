# frozen_string_literal: true

require "open3"
require "tempfile"

module NeutriverseGitCapture
  module_function

  def capture(*command)
    Open3.capture3(*command)
  rescue Errno::EACCES
    capture_without_pipes(*command)
  end

  def capture_without_pipes(*command)
    Tempfile.create("neutriverse-git-output-") do |output|
      Tempfile.create("neutriverse-git-error-") do |error|
        system(*command, out: output, err: error)
        status = $?
        output.rewind
        error.rewind
        [output.read, error.read, status]
      end
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  posts_by_path = site.posts.docs.to_h do |post|
    relative_path = post.relative_path.delete_prefix("/").tr("\\", "/")
    [relative_path, post]
  end

  next if posts_by_path.empty?

  marker = "__NEUTRIVERSE_COMMIT__"
  output, error, status = NeutriverseGitCapture.capture(
    "git",
    "-c",
    "core.quotepath=false",
    "-C",
    site.source,
    "log",
    "--format=#{marker}%aI",
    "--name-only",
    "--",
    *posts_by_path.keys
  )

  unless status.success?
    message = error.lines.first&.strip || "git log exited with status #{status.exitstatus}"
    Jekyll.logger.warn "Post timestamps:", message
    next
  end

  history = Hash.new { |entries, path| entries[path] = [] }
  commit_date = nil

  output.each_line do |line|
    value = line.chomp

    if value.start_with?(marker)
      commit_date = value.delete_prefix(marker)
    elsif commit_date && posts_by_path.key?(value) && history[value].length < 2
      history[value] << commit_date
    end
  end

  history.each do |path, dates|
    posts_by_path[path].data["last_modified_at"] = dates.first if dates.length > 1
  end
rescue SystemCallError => error
  Jekyll.logger.warn "Post timestamps:", error.message
end
