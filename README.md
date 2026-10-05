<!-- Generated from list.yml by tools/awesome_tern.py. Edit list.yml, not this file. -->

# Awesome Tern

> Plugins, apps, tools and resources for [Tern](https://stencil.so/tern), Stencil's terminal.

Tern is a Rust-native terminal from [Stencil](https://stencil.so). Shells, [omp](https://omp.sh) agents and browser panes keep running in a daemon when the window closes, and come back after a reboot. One session can be open on the desktop app, on iOS and in a WebGPU browser tab at the same time; typing in one shows up in the others.

Plugins are written in Luau, and any program can draw native UI through the Tern Surface Protocol (TSP). `tern remote serve` serves a remote machine's sessions over QUIC. Tern is in closed beta; you get in through the [waitlist](https://auth.stencil.so/waitlist?app=tern).

## Contents

- [Plugins](#plugins)
  - [Command lenses](#command-lenses)
  - [Blocks](#blocks)
  - [Window and workflow](#window-and-workflow)
  - [Official examples](#official-examples)
- [Native TSP apps](#native-tsp-apps)
- [Agent integrations](#agent-integrations)
- [SDKs and protocol libraries](#sdks-and-protocol-libraries)
- [Official resources](#official-resources)
  - [Documentation](#documentation)
- [Packaging](#packaging)
- [Configs and dotfiles](#configs-and-dotfiles)

## Plugins

Tern plugins are written in Luau and can be installed directly from GitHub with `tern plugin install github.com/OWNER/REPO`. See the [plugin CLI reference](https://docs.stencil.so/tern/reference/cli.html) for the available commands.

### Command lenses

A lens captures a shell command's output and shows it as a native view. A Raw toggle shows the original text.

- [tern-jj](https://github.com/resYuto/tern-jj) - Displays `jj status` and `jj st` output as a read-only native card with added, modified and deleted files colored to match the Tern theme.

### Blocks

- [tern-spotify](https://github.com/rico-vz/tern-spotify) - Player block for the Spotify desktop app with cover art, playback, seeking and volume controls on macOS, Windows and Linux.
- [tern-video-block](https://github.com/verticalrectangle/tern-video-block) - Opens video files in a block with mpv sound, frame stepping and synced side-by-side playback using ffmpeg and the kitty graphics protocol.

### Window and workflow

Window plugins add commands, keybindings, layouts, and status-line segments.

- [tern-ide layout](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/layout.nix) - Window plugin with an IDE-style four-pane layout, set split ratios, and an omp pane, packaged with Nix inside a NixOS config.
- [tern-jj workspaces](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/jj.nix) - Creates, opens, removes, and inspects jj workspaces using Tern dialogs, tabs, and the status line, packaged with Nix inside a NixOS config.
- [herdr-tern-plugin](https://github.com/gabrielmoreira/herdr-tern-plugin) - Adds an Open Herdr Session command that picks an existing herdr session and attaches to it inside Tern without copying or converting workspaces.
- [tern-model-usage](https://github.com/azmifarih/tern-model-usage) - Shows omp coding-plan quota for each signed-in account in the status line and opens a canvas pane with provider cards and reset countdowns.

### Official examples

These examples ship with the official [SDK archive](https://docs.stencil.so/tern/tern-sdk.tar.gz). They are a good starting point if you are writing your own plugin.

- [Terraform Plans](https://docs.stencil.so/tern/examples/terraform.html) - Lens for `terraform plan` and `tofu plan` that shows badges, diagnostics and resources grouped by action.
- [Review Queue](https://docs.stencil.so/tern/examples/review-queue.html) - Block that polls `gh` every two minutes and lists pull requests waiting for your review.
- [JSON Explorer](https://docs.stencil.so/tern/examples/jsonx.html) - Opens JSON and GeoJSON files as collapsible trees and copies the jq path of a node.
- [Long-Running Commands](https://docs.stencil.so/tern/examples/longrun.html) - Shows a toast when slow commands finish, keeps a history of run times and status, and adds a status-line segment.
- [Directory Variables](https://docs.stencil.so/tern/examples/dirvars.html) - Loads approved `.tern-env` files into new shells and signals when a directory's environment changed.
- [Project Workspaces](https://docs.stencil.so/tern/examples/workspaces.html) - Builds named tabs and split panes from `.tern/workspace.json`.
- [Canvas Dashboard](https://docs.stencil.so/tern/reference/api-window.html#canvas-cx) - Window-only persistent dashboard that shows canvas ownership, keyed patches, and a Refresh action.

## Native TSP apps

Applications that draw their own user interface natively inside Tern using the Tern Surface Protocol (TSP).

- [oh-my-pi (omp)](https://github.com/can1357/oh-my-pi) - Stencil's coding agent that Tern is built around, drawing its transcript and UI natively, restoring sessions, and opening web pages as browser picture-in-picture panes.
- [Octet](https://github.com/skaft-software/octet/pull/485) - Coding-agent shell that renders transcript cards, split diffs, pickers, and reports through TSP, with Tern support merged into a feature branch, not `main`.
- [saavy](https://github.com/saavy1/saavy_cloud) - Persistent coding agent on Cloudflare with a native TSP frontend in Tern and a `pi-tui` fallback elsewhere.
- [Terngram](https://github.com/d3d0n/terngram) - Unofficial keyboard-driven Telegram client built on TDLib and omp's UI toolkit, also installable as a Tern plugin.

## Agent integrations

- [omp-side](https://github.com/wolfiesch/omp-side) - Adds a `/side` command to fork the conversation into a child session and open it in a side pane in Tern, cmux, tmux, WezTerm, Kitty, and Ghostty.
- [tern-mcp](https://github.com/NaC-L/tern-mcp) - Python MCP server over stdio wrapping the tern CLI with 14 tools for sessions, panes, capture, process inspection, input and layout.
- [tern-control](https://github.com/wolfiesch/tern-control) - An omp and Pi extension giving agents tools to find Tern sessions, read transcript digests, follow daemon events, change layout, and type into terminals.
- [omp-thinking-translator](https://github.com/Mouriya-Emma/omp-thinking-translator) - An omp extension that translates visible thinking into collapsible native sections in Tern and plain ANSI output in other terminals.

## SDKs and protocol libraries

- [Tern SDK](https://docs.stencil.so/tern/tern-sdk.tar.gz) - Official archive containing Luau type definitions (`tern.d.luau`) and example plugins.
- [@oh-my-pi/pi-wire](https://github.com/can1357/oh-my-pi/tree/main/packages/wire) - TypeScript package implementing the TSP wire format: APC framing, component types, frame operations, handshake and events.
- [@oh-my-pi/pi-tui](https://github.com/can1357/oh-my-pi/tree/main/packages/tui) - TypeScript UI toolkit from omp for rendering transcripts, chat, dashboards, and pickers natively over TSP.
- [octet-tern](https://github.com/skaft-software/octet/tree/9e8abda1f4f210d43361b6c0a80e482097feff77/crates/octet-tern) - A Rust TSP client built into Octet with wire types, APC chunking, tty flow control, and scene builders.

## Official resources

- [Tern](https://stencil.so/tern) - Stencil's product page for Tern with a feature tour.
- [Waitlist](https://auth.stencil.so/waitlist?app=tern) - Sign up for Tern's closed beta using a Stencil account.
- [Beta builds](https://build.stencil.so/tern) - CI-generated beta builds from the `main` branch, requiring sign-in.
- [Stencil on GitHub](https://github.com/stencil-hq) - Stencil's GitHub organization; Tern's source is not public.
- [@stencil_labs](https://x.com/stencil_labs) - Stencil's account on X.
- [@_can1357](https://x.com/_can1357) - Stencil founder Can Bölük on X, where he posts most Tern announcements.
- [omp Discord](https://discord.gg/4NMW9cdXZa) - The community Discord server for omp, where Tern is also discussed.

### Documentation

- [Tern plugin book](https://docs.stencil.so/tern/) - Official documentation covering host and window runtimes, lenses, blocks, native views, styling, and TSP.
- [Getting Started](https://docs.stencil.so/tern/guides/getting-started.html) - Walkthrough of building a lens and palette command, then linking, type-checking, and reloading.
- [Command Lenses](https://docs.stencil.so/tern/guides/lenses.html) - Explains how to turn command output into native views using manifest globs and host callbacks.
- [Debugging](https://docs.stencil.so/tern/guides/debugging.html) - Covers toasts, logs, Luau typing, handler budgets, and scripted window control.
- [Plugin CLI](https://docs.stencil.so/tern/reference/cli.html) - Reference for `tern plugin list`, `install`, `link`, `unlink`, `remove`, `reload`, `dir`, and `types`.
- [Tern Surface Protocol](https://docs.stencil.so/tern/protocol/index.html) - Specifies the in-band protocol where CLIs, TUIs, and agents send UI trees that Tern lays out and draws natively.

## Packaging

Tern builds are behind a sign-in, so most of these packages expect you to download the build yourself.

- [pelikanade/flake](https://github.com/pelikanade/flake/blob/f6f8217278a4a119c8e3a5b27b5a30ffef57cbd1/docs/tern.md) - Nix packaging guide covering signed-in downloads, `requireFile`, graphics libraries, and updating.
- [not-matthias/dotfiles-nix](https://github.com/not-matthias/dotfiles-nix/blob/c1c7f09f29c1c938df834427bb96034b2502530e/pkgs/tern.nix) - Provides a Nix derivation for x86_64 Linux that uses requireFile and autoPatchelf.
- [tdortman/dotfiles](https://github.com/tdortman/dotfiles/blob/008242f1f3ef305950a98f9878a0253477f256b0/nix/packages/tern/default.nix) - Nix package with desktop entries and an update script that finds new builds using a Stencil browser session.
- [install-tern-nixos.sh](https://github.com/4weaver/nixdots/blob/a326859f4ba07920d205b2f88a3fd7af8922d92f/scripts/install-tern-nixos.sh) - Shell script that patches the Linux tarball for NixOS and runs `tern remote serve` as a user service on UDP port 8376.
- [phibkro/homelab](https://github.com/phibkro/homelab/blob/1741e8cd636c483dda04ece696d57c1f9efbea9a/src/users/nori/programs/tern/default.nix) - Nix package for Tern 0.4.1 that patches graphics and input library paths.

## Configs and dotfiles

- [plumj-am/nixos](https://github.com/plumj-am/nixos/blob/master/modules/tern.nix) - NixOS module that manages Tern settings, theme, tmux-style keybindings, the `omp` launch command and plugins.
- [tdortman Tern launcher](https://github.com/tdortman/dotfiles/blob/008242f1f3ef305950a98f9878a0253477f256b0/nix/modules/home/tern/default.nix) - Home Manager module that uses Meta+Return to focus the open Tern window on KDE Plasma or start Tern.

## Contributing

Suggestions are welcome as pull requests. Read the [contribution guidelines](CONTRIBUTING.md) first.
