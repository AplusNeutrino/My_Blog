# frozen_string_literal: true

# The local Windows Ruby environment can fail to expand Liquid's tag glob,
# leaving standard tags such as `if` unregistered. Load them explicitly.
%w[
  assign
  break
  capture
  case
  comment
  continue
  cycle
  decrement
  for
  if
  ifchanged
  increment
  raw
  table_row
  unless
].each { |tag| require "liquid/tags/#{tag}" }
