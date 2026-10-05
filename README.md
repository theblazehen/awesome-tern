# Awesome Tern [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of plugins, apps, tools, and resources for [Tern](https://stencil.so/tern), the Rust-native "neoterminal" from [Stencil](https://stencil.so).

Tern keeps shells, [omp](https://omp.sh) agents, and browser panes running in a daemon that outlives the window. Sessions are shared live across the desktop app, iOS, and a WebGPU browser tab, and can be served from remote hosts over QUIC. Plugins are written in Luau, and any program can draw native UI through the **Tern Surface Protocol (TSP)**.

Tern is in **closed beta**. Join the [waitlist](https://auth.stencil.so/waitlist?app=tern) to get access.

## Contents

- [Plugins](#plugins)
  - [Command lenses](#command-lenses)
  - [Blocks](#blocks)
  - [Window and workflow](#window-and-workflow)
  - [Official example plugins](#official-example-plugins)
- [Native TSP apps](#native-tsp-apps)
- [Agent integrations](#agent-integrations)
- [SDKs and protocol libraries](#sdks-and-protocol-libraries)
- [Official resources](#official-resources)
  - [Documentation](#documentation)
- [Packaging and installation](#packaging-and-installation)
- [Configs and dotfiles](#configs-and-dotfiles)
- [Announcements and release notes](#announcements-and-release-notes)
- [Community](#community)
- [Contributing](#contributing)

## Plugins

Install any GitHub-hosted plugin with `tern plugin install github.com/OWNER/REPO`. See the [plugin CLI reference](https://docs.stencil.so/tern/reference/cli.html).

### Command lenses

Lenses capture a shell command's output and render it as a native view, with a Raw toggle back to the original text.

- [tern-jj](https://github.com/resYuto/tern-jj) - Renders `jj status` as a themed native Jujutsu status card. Also a well-documented dev setup with mise, luau-lsp, and smoke tests.

### Blocks

- [tern-video-block](https://github.com/verticalrectangle/tern-video-block) - Plays video files in a block with sound, frame stepping, and synced side-by-side playback (ffmpeg + mpv, kitty graphics protocol).
- [tern-spotify](https://github.com/rico-vz/tern-spotify) - Native Spotify desktop-player block with cover art, playback, seeking, and volume controls on macOS, Windows, and Linux.

### Window and workflow

- [tern-model-usage](https://github.com/azmifarih/tern-model-usage) - Shows omp coding-plan quotas for every account in the status line, plus a detailed Model Usage canvas pane.
- [herdr-tern-plugin](https://github.com/gabrielmoreira/herdr-tern-plugin) - Adds an "Open Herdr Session" command that picks and attaches existing [herdr](https://github.com/ogulcancelik/herdr) sessions inside Tern.
- [tern-ide layout](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/layout.nix) - IDE-like four-cell layout with explicit split ratios and an omp pane. Nix-packaged, embedded in dotfiles.
- [tern-jj workspaces](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/jj.nix) - Creates, opens, removes, and inspects Jujutsu workspaces through Tern dialogs, tabs, and the status line. Nix-packaged, embedded in dotfiles.

### Official example plugins

These ship in the official [SDK archive](https://docs.stencil.so/tern/tern-sdk.tar.gz) and are good references for writing your own.

- [Terraform Plans](https://docs.stencil.so/tern/examples/terraform.html) - Lens rendering `terraform plan` / `tofu plan` as badges, diagnostics, and resources grouped by action.
- [Review Queue](https://docs.stencil.so/tern/examples/review-queue.html) - Polls `gh` for pull requests awaiting your review and shows them in a native block.
- [JSON Explorer](https://docs.stencil.so/tern/examples/jsonx.html) - Opens JSON and GeoJSON files as collapsible native trees with jq-path copying.
- [Long-Running Commands](https://docs.stencil.so/tern/examples/longrun.html) - Toasts when slow commands finish and tracks their history and status.
- [Directory Variables](https://docs.stencil.so/tern/examples/dirvars.html) - Injects approved `.tern-env` files into new shells.
- [Project Workspaces](https://docs.stencil.so/tern/examples/workspaces.html) - Builds named tabs and split panes from `.tern/workspace.json`.
- [Canvas Dashboard](https://docs.stencil.so/tern/reference/api-window.html#canvas-cx) - Persistent window canvas showing ownership, keyed patches, and Refresh actions.

## Native TSP apps

Programs that draw their UI natively in Tern over the Tern Surface Protocol.

- [oh-my-pi (omp)](https://github.com/can1357/oh-my-pi) - Stencil's coding agent, Tern's flagship native app: native transcript UI, session restore through the daemon, and browser picture-in-picture panes.
- [Terngram](https://github.com/d3d0n/terngram) - Keyboard-first unofficial Telegram client built on TDLib and omp's native UI toolkit. Also installable as a Tern plugin.
- [saavy](https://github.com/saavy1/saavy_cloud) - Cloudflare-backed persistent coding agent with a native TSP frontend that falls back to pi-tui outside Tern.
- [Octet](https://github.com/skaft-software/octet/pull/485) - Coding-agent shell that renders transcript cards, split diffs, pickers, and reports through TSP. Merged to a feature branch, not yet on `main`.

## Agent integrations

- [tern-control](https://github.com/wolfiesch/tern-control) - omp/Pi extension giving agents typed Tern session discovery, transcript digests, daemon events, layout control, and terminal input.
- [tern-mcp](https://github.com/NaC-L/tern-mcp) - Python stdio MCP server that wraps the Tern CLI with 14 tools for sessions, panes, capture, input, and layout.
- [omp-thinking-translator](https://github.com/Mouriya-Emma/omp-thinking-translator) - omp extension that shows translated thinking as native collapsible TSP sections in Tern, with an ANSI fallback elsewhere.

## SDKs and protocol libraries

- [Official Tern SDK](https://docs.stencil.so/tern/tern-sdk.tar.gz) - Luau type definitions (`tern.d.luau`) plus the installable example plugins.
- [@oh-my-pi/pi-wire](https://github.com/can1357/oh-my-pi/tree/main/packages/wire) - TypeScript TSP wire contract: APC framing, component types, frame operations, handshake, and events.
- [@oh-my-pi/pi-tui](https://github.com/can1357/oh-my-pi/tree/main/packages/tui) - omp's UI toolkit with native TSP rendering for transcripts, chat, dashboards, and pickers.
- [octet-tern](https://github.com/skaft-software/octet/tree/9e8abda1f4f210d43361b6c0a80e482097feff77/crates/octet-tern) - Rust TSP client with wire types, APC chunking, tty flow control, and scene builders. Octet-specific, not a standalone crate.

## Official resources

- [Tern](https://stencil.so/tern) - Product page and feature tour.
- [Waitlist](https://auth.stencil.so/waitlist?app=tern) - Request closed-beta access with a Stencil account.
- [Beta builds](https://build.stencil.so/tern) - Early builds published by CI from `main`. Sign-in required.
- [Stencil on GitHub](https://github.com/stencil-hq) - Stencil's organization. Tern's source is not public.
- [@stencil_labs](https://x.com/stencil_labs) - Stencil on X.
- [@_can1357](https://x.com/_can1357) - Can Bölük, Stencil founder, who posts most Tern announcements.
- [omp Discord](https://discord.gg/4NMW9cdXZa) - Community server for omp, where Tern is discussed too.

### Documentation

- [Tern plugin book](https://docs.stencil.so/tern/) - Host and window runtimes, lenses, blocks, native views, styling, and TSP. Full [table of contents](https://docs.stencil.so/tern/toc.html).
- [Getting Started](https://docs.stencil.so/tern/guides/getting-started.html) - Build a first lens and palette command, then link, type-check, and reload it.
- [Command Lenses](https://docs.stencil.so/tern/guides/lenses.html) - Turn shell command output into native views with manifest globs and host callbacks.
- [Debugging](https://docs.stencil.so/tern/guides/debugging.html) - Toasts, logs, Luau typing, handler budgets, and scripted window control.
- [Plugin CLI](https://docs.stencil.so/tern/reference/cli.html) - `tern plugin list|install|link|unlink|remove|reload|dir|types`.
- [Tern Surface Protocol](https://docs.stencil.so/tern/protocol/index.html) - Spec for the in-band protocol that lets CLIs, TUIs, and agents send semantic UI trees for Tern to render natively.

## Packaging and installation

- [pelikanade/flake](https://github.com/pelikanade/flake/blob/f6f8217278a4a119c8e3a5b27b5a30ffef57cbd1/docs/tern.md) - Nix packaging guide for Tern 0.4.4 covering authenticated downloads, `requireFile`, runtime graphics libraries, and updates.
- [tdortman/dotfiles](https://github.com/tdortman/dotfiles/blob/008242f1f3ef305950a98f9878a0253477f256b0/nix/packages/tern/default.nix) - Nix package for Tern 0.4.5 with desktop entries, plus an [updater script](https://github.com/tdortman/dotfiles/blob/008242f1f3ef305950a98f9878a0253477f256b0/nix/packages/tern/update.sh) that finds new authenticated builds.
- [not-matthias/dotfiles-nix](https://github.com/not-matthias/dotfiles-nix/blob/c1c7f09f29c1c938df834427bb96034b2502530e/pkgs/tern.nix) - Nix derivation for x86_64 Linux using `requireFile` and `autoPatchelf`.
- [phibkro/homelab](https://github.com/phibkro/homelab/blob/1741e8cd636c483dda04ece696d57c1f9efbea9a/src/users/nori/programs/tern/default.nix) - Nix package for Tern 0.4.1 with patched graphics and input runtime paths.
- [install-tern-nixos.sh](https://github.com/4weaver/nixdots/blob/a326859f4ba07920d205b2f88a3fd7af8922d92f/scripts/install-tern-nixos.sh) - Script that patches the Linux tarball for NixOS and runs `tern remote serve` as a user service (UDP 8376).

## Configs and dotfiles

- [plumj-am/nixos](https://github.com/plumj-am/nixos/blob/master/modules/tern.nix) - NixOS module managing Tern settings, themes, tmux-style keybindings, the omp launch command, and plugin installation.
- [tdortman Tern focus launcher](https://github.com/tdortman/dotfiles/blob/008242f1f3ef305950a98f9878a0253477f256b0/nix/modules/home/tern/default.nix) - Home Manager module binding Meta+Return to focus or launch Tern on KDE Plasma.

## Announcements and release notes

- [Feature-complete beta](https://x.com/_can1357/status/2105052776288137367) - Persistent sessions, QUIC remoting over Tailscale/iroh, shared desktop/iOS/web sessions, browser panes, and native components (2026-09-29).
- [v0.2.1 changelog](https://x.com/_can1357/status/2105537028461084712) - First beta feedback round (2026-10-01).
- [Git and SQLite blocks](https://x.com/_can1357/status/2105870359585321344) - Preview of the Git and SQLite blocks and the refreshed dark appearance (2026-10-02).
- [v0.2.8: notebooks](https://x.com/_can1357/status/2106012792767844538) - Notebook support and fixes (2026-10-02).
- [Profiler](https://x.com/_can1357/status/2106617663778697480) - Built-in profiler demo (2026-10-04).
- [omp v18.4.4](https://github.com/can1357/oh-my-pi/releases/tag/v18.4.4) - Introduces TSP rendering, Tern session restore, and native browser picture-in-picture in omp.
- [omp releases](https://github.com/can1357/oh-my-pi/releases) - Ongoing Tern integration work: [v18.4.6](https://github.com/can1357/oh-my-pi/releases/tag/v18.4.6), [v18.4.9](https://github.com/can1357/oh-my-pi/releases/tag/v18.4.9), [v18.5.0](https://github.com/can1357/oh-my-pi/releases/tag/v18.5.0), [v18.6.0](https://github.com/can1357/oh-my-pi/releases/tag/v18.6.0), [v18.6.1](https://github.com/can1357/oh-my-pi/releases/tag/v18.6.1).

## Community

Demos, reactions, and feedback.

- [Tern opening omp on macOS](https://x.com/epsilver_/status/2105512072289431740) - @epsilver_'s first look. A reply describes adding TSP support to another agent.
- [Theme showcase](https://x.com/epsilver_/status/2105517407259578568) - @epsilver_ tours Tern's built-in themes.
- [Git block on Linux](https://x.com/epsilver_/status/2106073853097066718) - @epsilver_ uses the Git block to review changes after long omp sessions.
- [omp questionnaires in Tern](https://x.com/epsilver_/status/2106382839876882847) - @epsilver_ on native questionnaire rendering, compared with cmux.
- [Custom video block](https://x.com/epsilver_/status/2107005258345906247) - @epsilver_ shows the video block that became [tern-video-block](https://github.com/verticalrectangle/tern-video-block).
- [Tern + omp first impressions](https://x.com/fullctx/status/2106588132355502329) - @fullctx on Tern as "omp desktop", with waitlist discussion.
- [Tern is mind-blowing](https://x.com/alxfazio/status/2106832630616670696) - @alxfazio's reaction. Replies cover SSH colors and plugin development.
- [Tern vs cmux](https://x.com/wolfie_/status/2105512364888244376) - @wolfie_ compares the two and explains omp (the harness) vs Tern (the multiplexer).
- [Japanese IME feedback](https://x.com/ryosuz16/status/2105949827746124129) - @ryosuz16 reports that composing Japanese text isn't displayed yet.
- [Beta testing Tern as omp's GUI](https://x.com/julie_bush/status/2105909146273128514) - @julie_bush on the beta.
- [Is Tern the Raycast of terminals?](https://www.threads.com/@unclejobs.ai/post/DeBibr8iS4z) - Korean hands-on post on Tern's interface and the shift back to native apps.

## Contributing

Contributions are welcome. Read the [contribution guidelines](CONTRIBUTING.md) first.
