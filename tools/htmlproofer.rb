# frozen_string_literal: true

# html-proofer eagerly loads its external URL validator even when external
# checks are disabled. Avoid loading Typhoeus/libcurl for this internal-only
# validation command.
module Typhoeus
end

$LOADED_FEATURES << "typhoeus.rb"

require "html-proofer"

# html-proofer 5.2.1 processes files concurrently while keeping the current
# document and filename on the shared Runner. Process files in order so a
# check can never observe another document's state.
module SequentialHTMLProofer
  def process_files
    files.map { |file| load_file(file[:path], file[:source]) }
  end
end

HTMLProofer::Runner.prepend(SequentialHTMLProofer)

site_dir = ARGV.fetch(0, "_site")
options = {
  disable_external: true,
  ignore_urls: [
    %r{\Ahttp://127\.0\.0\.1},
    %r{\Ahttp://0\.0\.0\.0},
    %r{\Ahttp://localhost},
  ],
}

HTMLProofer.check_directory(site_dir, options).run
