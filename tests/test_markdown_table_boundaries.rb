require 'minitest/autorun'
require 'kramdown'
require 'kramdown-parser-gfm'
require_relative '../_plugins/markdown-table-boundaries'

class TestMarkdownTableBoundaries < Minitest::Test
  def normalize(text)
    NeutriverseTableBoundaries.normalize(text)
  end

  def test_heading_adjacent_table_renders_without_editing_source
    source = "## Heading\n| A | B |\n| --- | --- |\n| one | two |\n"
    original = source.dup
    assert_includes Kramdown::Document.new(normalize(source), input: 'GFM').to_html, '<table>'
    assert_equal original, source
    assert_equal normalize(source), normalize(normalize(source))
  end

  def test_fenced_example_remains_literal
    %w[``` ~~~~].each do |fence|
      source = "#{fence}markdown\n## Example\n| A | B |\n| --- | --- |\n#{fence}\n"
      assert_equal source, normalize(source)
    end
  end

  def test_ordinary_prose_and_existing_blank_boundary_are_unchanged
    ["Prose\n| A | B |\n| --- | --- |\n", "## Heading\n\n| A | B |\n| --- | --- |\n",
     "## Heading\n| A | B |\n| bad | separator |\n"].each do |source|
      assert_equal source, normalize(source)
    end
  end

  def test_actual_public_article_produces_two_tables
    path = File.expand_path('../_posts/2025-04-16-计组-04.md', __dir__)
    source = File.read(path).sub(/\A---\s*\n.*?\n---\s*\n/m, '')
    html = Kramdown::Document.new(normalize(source), input: 'GFM').to_html
    assert_equal 2, html.scan('<table>').length
    assert_includes html, 'EA = (SP)'
    assert_includes html, 'CISC'
  end
end
