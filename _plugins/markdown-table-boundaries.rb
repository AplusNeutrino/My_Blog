# Render-only compatibility for legacy tables immediately after ATX headings.
# Source files and their protected body hashes must remain untouched.
module NeutriverseTableBoundaries
  def self.normalize(content)
    lines = content.lines
    fence = nil
    output = []
    lines.each_with_index do |line, index|
      marker = line.match(/^ {0,3}(`{3,}|~{3,})/)
      if marker
        token = marker[1]
        if fence.nil?
          fence = token
        elsif token[0] == fence[0] && token.length >= fence.length
          fence = nil
        end
      end
      if fence.nil? && line.match?(/^ {0,3}\|/) &&
         output.last&.match?(/^ {0,3}\#{1,6}\s+\S/) &&
         delimiter?(lines[index + 1])
        output << "\n"
      end
      output << line
    end
    output.join
  end

  def self.delimiter?(line)
    return false unless line
    cells = line.strip.sub(/^\|/, '').sub(/\|$/, '').split('|', -1)
    cells.length >= 2 && cells.all? { |cell| cell.strip.match?(/^:?-{3,}:?$/) }
  end
end

if defined?(Jekyll::Hooks)
  Jekyll::Hooks.register :posts, :pre_render do |post|
    next unless %w[.md .markdown].include?(post.extname.downcase)
    post.content = NeutriverseTableBoundaries.normalize(post.content)
  end
end
