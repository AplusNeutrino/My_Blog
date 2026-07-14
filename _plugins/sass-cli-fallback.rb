# frozen_string_literal: true

require "tempfile"

module NeutriverseSassCliFallback
  module_function

  def enabled?
    return true if ENV["JEKYLL_SASS_CLI_FALLBACK"] == "1"

    reader, writer = IO.pipe
    reader.close
    writer.close
    false
  rescue Errno::EACCES
    true
  end

  def command
    sass_root = Gem.loaded_specs.fetch("sass-embedded").full_gem_path
    dart_sass_root = File.join(sass_root, "lib", "sass", "dart-sass")
    launcher = File.join(dart_sass_root, "sass")
    dart = File.join(dart_sass_root, "src", Gem.win_platform? ? "dart.exe" : "dart")
    snapshot = File.join(dart_sass_root, "src", "sass.snapshot")

    return [launcher] if File.executable?(launcher)
    return [dart, snapshot] if File.executable?(dart) && File.file?(snapshot)

    raise Jekyll::Errors::FatalException, "Unable to locate the Dart Sass CLI bundled with sass-embedded."
  end

  module Converter
    def convert(content)
      Tempfile.create(["jekyll-sass-input-", ".scss"]) do |input|
        Tempfile.create(["jekyll-sass-output-", ".css"]) do |output|
          Tempfile.create(["jekyll-sass-error-", ".log"]) do |error|
            input.write(content)
            input.flush
            output.close
            error.close

            sass_command = NeutriverseSassCliFallback.command
            sass_command.concat(["--style=#{sass_style}", "--no-source-map"])
            sass_load_paths.each { |path| sass_command.concat(["--load-path", path]) }
            sass_command.concat([input.path, output.path])

            success = system(*sass_command, out: File::NULL, err: error.path)
            diagnostics = File.read(error.path, encoding: "UTF-8").strip

            unless success
              message = diagnostics.empty? ? "Dart Sass CLI failed." : diagnostics
              raise Jekyll::Converters::Scss::SyntaxError, message
            end

            Jekyll.logger.debug "Sass CLI fallback:", diagnostics unless diagnostics.empty?
            File.read(output.path, encoding: "UTF-8")
          end
        end
      end
    end
  end
end

if NeutriverseSassCliFallback.enabled?
  Jekyll::Converters::Scss.prepend(NeutriverseSassCliFallback::Converter)
end
