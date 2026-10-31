<!-- Generated from list.yml by tools/awesome_tern.py. Edit list.yml, not this file. -->

# Awesome Tern

> Plugins, apps, tools and resources for [Tern](https://stencil.so/tern), Stencil's terminal.

Tern is a Rust-native terminal from [Stencil](https://stencil.so). Shells, [omp](https://omp.sh) agents and browser panes keep running in a daemon when the window closes, and come back after a reboot. One session can be open on the desktop app, on iOS and in a WebGPU browser tab at the same time; typing in one shows up in the others. `tern remote serve` serves a remote machine's sessions over QUIC.

Tern is in closed beta; request access through the [waitlist](https://auth.stencil.so/waitlist?app=tern), and join the discussion in the [omp Discord](https://discord.gg/4NMW9cdXZa).

Plugins are written in Luau and installed with `tern plugin install github.com/OWNER/REPO` (see the [plugin CLI reference](https://docs.stencil.so/tern/reference/cli.html)). Apps are standalone programs that draw their own UI in a Tern pane over the Tern Surface Protocol (TSP); install them as their README describes.

Each entry shows what kind of project it is, its GitHub stars and how long ago it was last updated; the [legend](#legend) explains the labels.

## Contents

- **[Agents](#agents)** 55 — [Coding agents](#coding-agents) · [Agent extensions](#agent-extensions) · [Usage and quotas](#usage-and-quotas) · [Status and dashboards](#status-and-dashboards) · [Orchestration](#orchestration) · [Worktrees](#worktrees) · [Notifications and alerts](#notifications-and-alerts)
- **[Workspace](#workspace)** 37 — [Sessions and sidebars](#sessions-and-sidebars) · [Navigation, layout and input](#navigation-layout-and-input) · [Integrations](#integrations) · [Remote hosts](#remote-hosts) · [Companion apps](#companion-apps) · [Themes and appearance](#themes-and-appearance) · [Localization](#localization)
- **[Development](#development)** 35 — [Git](#git) · [Review and feedback](#review-and-feedback) · [Issues and tasks](#issues-and-tasks) · [File viewers and notebooks](#file-viewers-and-notebooks) · [Cloud and data](#cloud-and-data) · [System and developer tools](#system-and-developer-tools)
- **[Media and fun](#media-and-fun)** 18 — [Music and media](#music-and-media) · [Fun](#fun) · [Other](#other)
- **[Building for Tern](#building-for-tern)** 11 — [Documentation](#documentation) · [SDKs and protocol libraries](#sdks-and-protocol-libraries) · [Plugin templates and tooling](#plugin-templates-and-tooling)
- **[Packaging and dotfiles](#packaging-and-dotfiles)** 4

## Agents

*Coding agents that draw natively in Tern, extensions that make agents Tern-aware, and plugins for watching and steering them.*

### Coding agents

| Project | About |
|---|---|
| **[oh-my-pi (omp)](https://github.com/can1357/oh-my-pi)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 37.3k` `today` | Stencil's coding agent that Tern is built around, drawing its transcript and UI natively, restoring sessions, and opening web pages as browser picture-in-picture panes.<details><summary>Screenshot</summary><img src="https://github.com/can1357/oh-my-pi/raw/main/assets/python.webp" width="520" alt="oh-my-pi (omp) screenshot"></details> |
| **[Hermes for Tern](https://github.com/thefullctx/hermes-for-tern)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 22` `8d` | Unofficial Tern frontend for Hermes Agent that draws the conversation, tool rows, subagents, buttons and a docked composer natively over TSP, and leaves the normal Hermes interface alone in other terminals.<details><summary>Screenshot</summary><img src="https://github.com/thefullctx/hermes-for-tern/raw/main/assets/screenshot.png" width="520" alt="Hermes for Tern screenshot"></details> |
| **[Octet](https://github.com/skaft-software/octet/pull/485)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 10` `1d` | Coding-agent shell rendering transcript cards, split diffs, pickers, and reports through TSP; Tern support is merged into the integration branch for 0.8.2 but not in the latest 0.8.1 release. |
| **[saavy](https://github.com/saavy1/saavy_cloud)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 2` `3w` | Persistent coding agent on Cloudflare with a native TSP frontend in Tern and a `pi-tui` fallback elsewhere. |
| **[codex-tern](https://github.com/juniorxxue/codex-tern)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 1` `3d` | Unofficial Codex GUI that talks to the official `codex app-server` and draws its interface natively in Tern, keeping your existing Codex login and config.<details><summary>Screenshot</summary><img src="https://github.com/juniorxxue/codex-tern/raw/main/docs/images/writing-edits.png" width="520" alt="codex-tern screenshot"></details> |
| **[tern-agents-ui](https://github.com/saanuregh/tern-agents-ui)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 1` `10d` | Native chat frontends for Claude Code (`tclaude`) and Codex (`tcodex`) that draw the conversation, tool cards, subagents, plans, permission prompts and a composer with model, effort and context chips over TSP, and report agent status to Tern's attention inbox.<details><summary>Screenshot</summary><img src="https://github.com/saanuregh/tern-agents-ui/raw/main/docs/screenshot.png" width="520" alt="tern-agents-ui screenshot"></details> |

### Agent extensions

*These run inside your coding agent rather than inside Tern.*

| Project | About |
|---|---|
| **[omp-side](https://github.com/wolfiesch/omp-side)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 10` `9d` | Adds a `/side` command to fork the conversation into a child session and open it in a side pane in Tern, cmux, tmux, WezTerm, Kitty, and Ghostty. |
| **[pi-tern](https://github.com/Ghost-9/pi-tern)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 7` `today` | Makes the pi coding agent Tern-aware with the TSP handshake, native Mermaid diagrams, browser automation, pane capture and a session mirror. |
| **[omp-stretch](https://github.com/materemias/omp-stretch)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 6` `4d` | Shows each omp reply in Tern as its gist, with linked phrases that grow their detail in place when clicked, and tells the model which parts you opened.<details><summary>Screenshot</summary><img src="https://github.com/materemias/omp-stretch/raw/master/docs/stretch.gif" width="520" alt="omp-stretch screenshot"></details> |
| **[hermes-tern](https://github.com/alt-glitch/hermes-tern)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 4` `9d` | Hermes Agent plugin that adds `hermes tern`, drawing the transcript, tool cards, approvals, subagents and pull requests as native Tern UI.<details><summary>Screenshot</summary><img src="https://github.com/alt-glitch/hermes-tern/raw/main/docs/images/transcript.png" width="520" alt="hermes-tern screenshot"></details> |
| **[tern-mcp](https://github.com/NaC-L/tern-mcp)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 2` `4w` | Python MCP server over stdio wrapping the tern CLI with 14 tools for sessions, panes, capture, process inspection, input and layout. |
| **[tern-omp-bridge](https://github.com/theblazehen/tern-omp-bridge)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 2` `7d` | Gives omp agents a `tern_exec` tool that runs Luau in the live Tern window to inspect and control it and to show native tables, charts and buttons. |
| **[omp-thinking-translator](https://github.com/Mouriya-Emma/omp-thinking-translator)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 1` `5d` | An omp extension that translates visible thinking into collapsible native sections in Tern and plain ANSI output in other terminals. |
| **[tern-control](https://github.com/wolfiesch/tern-control)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 1` `4w` | An omp and Pi extension giving agents tools to find Tern sessions, read transcript digests, follow daemon events, change layout, and type into terminals. |
| **[tern-omp-vimnav](https://github.com/DinMon/tern-omp-vimnav)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 0` `3w` | Vim-style navigation of the omp transcript in Tern, with block cursor, text selection and copying, search and Vimium-style hints for links, code blocks and buttons.<details><summary>Screenshot</summary><img src="https://github.com/DinMon/tern-omp-vimnav/raw/main/docs/vimnav-demo.webp" width="520" alt="tern-omp-vimnav screenshot"></details> |

### Usage and quotas

| Project | About |
|---|---|
| **[tern-plugin-omp-usage](https://github.com/jmazzola/tern-plugin-omp-usage)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 6` `2w` | Shows omp usage limits above the composer's context bar, with a meter, reset countdown and clock time for each window on hover.<details><summary>Screenshot</summary><img src="https://github.com/jmazzola/tern-plugin-omp-usage/raw/main/docs/images/line-current.png" width="520" alt="tern-plugin-omp-usage screenshot"></details> |
| **[CodexBar AgentView](https://github.com/materemias/codexbar-agentview)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `6d` | Shows Claude, Codex and other AI provider usage from the CodexBar CLI in the status line, with a dashboard that lists live and ended Claude Code, Codex, omp and pi sessions and focuses or resumes them in Tern tabs.<details><summary>Screenshot</summary><img src="https://github.com/materemias/codexbar-agentview/raw/master/docs/kde.gif" width="520" alt="CodexBar AgentView screenshot"></details> |
| **[tern-ai-limits](https://github.com/pfTheTrial/tern-ai-limits)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `11d` | Side-column panel showing every usage window of your AI coding plans as a ring with its reset countdown, covering Claude, Codex, Cursor, Grok and anything omp tracks.<details><summary>Screenshot</summary><img src="https://github.com/pfTheTrial/tern-ai-limits/raw/main/screenshots/dashboard.png" width="520" alt="tern-ai-limits screenshot"></details> |
| **[tern-omp-usage](https://github.com/joaodutra88/tern-omp-usage)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `8d` | Shows Claude and Codex limits from omp in the status line as colored dots, with a work-week budget, alerts, a 7-day usage and cost dashboard and one-click updates.<details><summary>Screenshot</summary><img src="https://github.com/joaodutra88/tern-omp-usage/raw/main/assets/statusline.png" width="520" alt="tern-omp-usage screenshot"></details> |
| **[tern-usage-monitor](https://github.com/rico-vz/tern-usage-monitor)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Floating or docked panel showing usage for every omp linked account, with per-account quota bars, auto-refresh, ordering and update-time settings. |
| **[tern-omp-stats](https://github.com/BaLaurent/tern-omp-stats)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Dashboard block built from native components that turns the usage statistics in `~/.omp/stats.db` into per-model and per-project tables with cost.<details><summary>Screenshot</summary><img src="https://github.com/BaLaurent/tern-omp-stats/raw/main/docs/overview.png" width="520" alt="tern-omp-stats screenshot"></details> |
| **[tern-model-usage](https://github.com/azmifarih/tern-model-usage)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `3w` | Shows omp coding-plan quota for each signed-in account in the status line and opens a canvas pane with provider cards and reset countdowns. |
| **[omp-cache-meter](https://github.com/andreiverdes/omp-cache-meter)**<br><a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a><br>`★ 0` `3d` | Prompt-cache meter for omp with hits, writes and an expiry countdown, plus a Tern plugin that adds a status-line segment, tab countdowns and a toast before the cache goes cold.<details><summary>Screenshot</summary><img src="https://raw.githubusercontent.com/andreiverdes/agent-cache-meter/main/docs/screenshots/omp-meter-warm.png" width="520" alt="omp-cache-meter screenshot"></details> |
| **[tern-claude-usage](https://github.com/zerx-lab/tern-claude-usage)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Shows Claude Pro and Max usage limits in a panel and a status-line segment, with 5-hour and 7-day windows, per-model limits, pace tracking and reset countdowns.<details><summary>Screenshot</summary><img src="https://github.com/zerx-lab/tern-claude-usage/raw/main/assets/usage-panel.png" width="520" alt="tern-claude-usage screenshot"></details> |
| **[tern-minimax-quota](https://github.com/meisijiya/tern-minimax-quota)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `6d` | Shows your MiniMax Token Plan quota in the status line and refreshes it every five minutes.<details><summary>Screenshot</summary><img src="https://github.com/meisijiya/tern-minimax-quota/raw/main/docs/status-line.png" width="520" alt="tern-minimax-quota screenshot"></details> |
| **[tern-omp-usage-dashboard](https://github.com/wolfiesch/tern-omp-usage-dashboard)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `9d` | Native pane of omp provider quotas for every account, with remaining bars, reset countdowns and explicit login, stale and no-data states. |
| **[tern-plugins (Emirfs)](https://github.com/Emirfs/tern-plugins)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `9d` | Collection with a pane of remaining limits for every account across omp profiles, a display of which omp profile each pane runs, and a split-columns layout helper. |

### Status and dashboards

| Project | About |
|---|---|
| **[tern-software-factory](https://github.com/junaidrahim/tern-software-factory)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `5d` | Lists the agents on your Tern host and jumps to the pane of the one you select. |
| **[tern-tab-status](https://github.com/yoyooyooo/tern-tab-status)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Colors tabs by whether their omp and pi sessions are working, waiting or need your attention.<details><summary>Screenshot</summary><img src="https://github.com/yoyooyooo/tern-tab-status/raw/main/docs/images/tab-status-sidebar.png" width="520" alt="tern-tab-status screenshot"></details> |
| **[Agents Hub](https://github.com/plxzy/agents-hub/tree/main/plugins/tern-agents-hub)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `12d` | Side panel for a self-hosted Agents Hub that lists Pi agent runs with status, cost and pull request, lets you accept or reject pending reviews, and adds a status-line count. |
| **[omp Tiles](https://github.com/MrsKugla/omp-tiles-plugin)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Block with one colored tile per open omp session across all Tern sessions, showing the session title and whether it is working, waiting for you or idle. |
| **[tern-omp-trajectory](https://github.com/Ahaxzh/tern-omp-trajectory)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `10d` | Turns omp session logs into a native trajectory viewer with a turn-grouped call ledger, per-entry inspectors and a token timeline. |
| **[tern-periscope](https://github.com/kenXengineering/tern-periscope)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `8d` | Lists the subagents of an omp session with live status, tool counts and cost, and opens any transcript as it is written. |
| **[tern-agent-progress](https://github.com/Sipty/tern-agent-progress)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Marks tabs that run omp agents with WoW-style quest marks and todo progress bars.<details><summary>Screenshot</summary><img src="https://github.com/Sipty/tern-agent-progress/raw/main/docs/screenshot.png" width="520" alt="tern-agent-progress screenshot"></details> |
| **[tern-claude-workflows](https://github.com/cgasgarth/tern-claude-workflows)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `10d` | Side block that follows the Claude Code workflows of the session in its tab, with phase timelines, an agent tree with model, tokens, tools and idle time, and a table of past workflows; it also works for ACP chats, which do not show workflow progress.<details><summary>Screenshot</summary><img src="https://github.com/cgasgarth/tern-claude-workflows/raw/main/docs/screenshot.png" width="520" alt="tern-claude-workflows screenshot"></details> |
| **[tern-t3](https://github.com/rcnsh/tern-t3)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2d` | Reads, starts and replies to T3 Code agent threads in native Tern blocks.<details><summary>Screenshot</summary><img src="https://github.com/rcnsh/tern-t3/raw/main/docs/thread.png" width="520" alt="tern-t3 screenshot"></details> |

### Orchestration

| Project | About |
|---|---|
| **[tern-agent-scheduler](https://github.com/bmanturner/tern-agent-scheduler)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 20` `3d` | Schedules omp agent runs with cron, presets, plain-English or one-shot times, starts each in a background tab and keeps their results, failures and costs in a manager block, with status-line, notification and Carly support.<details><summary>Screenshot</summary><img src="https://github.com/bmanturner/tern-agent-scheduler/raw/main/docs/screenshots/manager-light.png" width="520" alt="tern-agent-scheduler screenshot"></details> |
| **[Overseer](https://github.com/mmnavarr/overseer)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 15` `2w` | Panel listing every branch in flight with its worktree, agents, pull request and ticket, where each worktree gets its own Tern session.<details><summary>Screenshot</summary><img src="https://github.com/mmnavarr/overseer/raw/main/docs/images/panel.png" width="520" alt="Overseer screenshot"></details> |
| **[tern-agents](https://github.com/maxtuzz/tern-agents)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Runs Claude Code, Codex, Gemini, OpenCode, Aider or any agent CLI as a Tern agent block, with profiles, run presets, a launcher and an Agents sidebar. |
| **[tern-swarm](https://github.com/bmanturner/tern-swarm)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Kanban board that runs omp agents on its cards in separate git worktrees, runs your checks on their work and waits for your approval. |
| **[tern-task-plugin](https://github.com/yesmeck/tern-task-plugin)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Makes each task a session with its own branch, git worktree and default agent, with a kanban dashboard of pull request status.<details><summary>Screenshot</summary><img src="https://github.com/yesmeck/tern-task-plugin/raw/main/docs/dashboard.png" width="520" alt="tern-task-plugin screenshot"></details> |
| **[Forge Projects](https://github.com/Moti-Velz/tern-forge/tree/main/projects)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Sidebar for parallel agent work that gives each git worktree its own Tern session, with agent status, pull request and Linear ticket on every row, and one box that opens or creates a worktree from a branch, ticket or pull request.<details><summary>Screenshot</summary><img src="https://github.com/Moti-Velz/tern-forge/raw/main/projects/docs/images/panel.png" width="520" alt="Forge Projects screenshot"></details> |
| **[tern-dsh-web](https://github.com/meisijiya/tern-dsh-web)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `6d` | Starts the DeepSeek Harness web UI on demand from a status-bar menu and opens it in a browser block, with restart, stop and update actions.<details><summary>Screenshot</summary><img src="https://github.com/meisijiya/tern-dsh-web/raw/master/docs/status-bar.png" width="520" alt="tern-dsh-web screenshot"></details> |

### Worktrees

| Project | About |
|---|---|
| **[tern-jj workspaces](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/jj.nix)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `1d` | Creates, opens, removes, and inspects jj workspaces using Tern dialogs, tabs, and the status line, packaged with Nix inside a NixOS config. |
| **[tern-worktree](https://github.com/nibblebot/tern-worktree)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Lists, opens and creates git worktrees from the command palette using plain git, with `jq` and a POSIX shell as the only other requirements.<details><summary>Screenshot</summary><img src="https://github.com/nibblebot/tern-worktree/raw/main/assets/worktree-demo.gif" width="520" alt="tern-worktree screenshot"></details> |
| **[tern-worktrees](https://github.com/riicodespretty/tern-worktrees)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `2w` | Opens git worktrees as Tern tabs with a branch picker and teardown on close, backed by a `tern-wt` CLI and an omp skill for agents. |
| **[Worktree Panel](https://github.com/mullerino/tern-worktree-panel)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Pins a panel to every tab that lists the git worktrees of the focused repository with the state of the omp agents in each, moves agents waiting for you to the top, and focuses or opens a worktree's tab on click.<details><summary>Screenshot</summary><img src="https://github.com/mullerino/tern-worktree-panel/raw/main/docs/panel.png" width="520" alt="Worktree Panel screenshot"></details> |
| **[tern-worktrees (aliefe04)](https://github.com/aliefe04/tern-worktrees)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`unavailable` | Adds palette commands that create a git worktree on a new branch with an agent tab, and remove the focused worktree only when it is clean and merged into the default branch. |

### Notifications and alerts

| Project | About |
|---|---|
| **[tern-chirp](https://github.com/Noctivoro/tern-chirp)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Plays a short synthesized beep when an agent finishes or waits for you, with the sound's shape chosen by Jev to match how the turn went.<details><summary>Screenshot</summary><img src="https://github.com/Noctivoro/tern-chirp/raw/main/.github/assets/sounds.jpg" width="520" alt="tern-chirp screenshot"></details> |
| **[tern-chime](https://github.com/H4vC/tern-chime)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Plays a configurable sound when a pane raises an unseen alert, an omp agent yields its turn, or a long command finishes, with bundled chimes and per-trigger overrides. |
| **[tern-haptic-alert](https://github.com/lfsmoura/tern-haptic-alert)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Sends a haptic pulse to a Logitech MX Master 4 when an agent finishes or is blocked waiting for input.<details><summary>Screenshot</summary><img src="https://github.com/lfsmoura/tern-haptic-alert/raw/main/assets/ternhaptic.png" width="520" alt="tern-haptic-alert screenshot"></details> |
| **[tern-bell](https://github.com/qiaoqinyu/tern-bell)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `9d` | Plays configurable sounds when a main agent completes, fails or needs input, with separate completion and failure selections, previewable macOS and custom sounds, and settings saved only on confirmation. |
| **[tern-desktop-pet](https://github.com/hanbong5938/tern-desktop-pet)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `8d` | Connects Tern agent observations and semantic asks to the separately installed Desktop Pet app. |
| **[tern-gpg-touch](https://github.com/edcnogueira/tern-gpg-touch)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Shows a toast, and optionally plays a sound, when a typed command starts that will wait for a touch on your GPG security key, with per-folder rules.<details><summary>Screenshot</summary><img src="https://github.com/edcnogueira/tern-gpg-touch/raw/main/docs/reminder.png" width="520" alt="tern-gpg-touch screenshot"></details> |
| **[tern-pushover](https://github.com/larkinwc/tern-pushover)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `5d` | Sends Pushover notifications to your phone when an agent needs you or finishes, or a long command ends, while you're away, with an Open Tern button. |

## Workspace

*Sessions, navigation and layout, remote hosts, and how Tern looks.*

### Sessions and sidebars

| Project | About |
|---|---|
| **[tern-projects](https://github.com/thegeneralist01/tern-projects)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 13` `2w` | Curated multi-folder projects, pinned chats, and search across OMP, Claude Code, Codex, Pi, OpenCode, and Cursor.<details><summary>Screenshot</summary><img src="https://github.com/thegeneralist01/tern-projects/raw/main/docs/screenshots/showcase-overview.png" width="520" alt="tern-projects screenshot"></details> |
| **[workspaces-sidebar](https://github.com/rezhajulio/workspaces-sidebar)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 5` `1d` | Pins a workspace sidebar to every tab that lists sessions and their tabs as a tree, with live badges for waiting agents, running and failed commands, one-click switching, tab color tags, and attention-jump keybindings.<details><summary>Screenshot</summary><img src="https://github.com/rezhajulio/workspaces-sidebar/raw/main/docs/demo.png" width="520" alt="workspaces-sidebar screenshot"></details> |
| **[Flock](https://github.com/Luqueee/flock)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `4d` | Groups omp agents, terminals and sessions by project and machine in a native sidebar, and opens an agent's git worktree in VS Code, locally or over SSH.<details><summary>Screenshot</summary><img src="https://github.com/Luqueee/flock/raw/main/docs/screenshot.png" width="520" alt="Flock screenshot"></details> |
| **[Kai](https://github.com/Yupmoh/tern-plugins/tree/main/kai)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Workspaces sidebar that shows each session as a card with its agents, files, git changes and branches.<details><summary>Screenshot</summary><img src="https://github.com/Yupmoh/tern-plugins/raw/main/kai/docs/images/sidebar.png" width="520" alt="Kai screenshot"></details> |
| **[tern-plugins (Unravl)](https://github.com/Unravl/tern-plugins)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `9d` | Collection with a left sidebar of sessions per host that shows omp agent status, and a fix that keeps the omp composer bar one band when macOS Reduce transparency is on. |
| **[tern-agent-nav](https://github.com/Arcadia822/tern-agent-nav)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `today` | Simple session sidebar in the style of Herdr that lists omp, Codex, Copilot and Claude Code agents grouped by Tern session, with a click to focus one.<details><summary>Screenshot</summary><img src="https://github.com/Arcadia822/tern-agent-nav/raw/main/docs/screenshot.png" width="520" alt="tern-agent-nav screenshot"></details> |
| **[tern-omp-groups](https://github.com/vishiod/tern-omp-groups)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `12d` | Groups omp chats by the code at the start of their titles and lists every saved chat under its group, reopening a closed one in that group with a click. |
| **[tern-workspaces-sidebar](https://github.com/tobiasesquivel/tern-workspaces-sidebar)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Sidebar that lists every session as a workspace with nested tabs, git counters and agent state, plus a small runtime that gives omp, Claude Code and Codex the same status. |

### Navigation, layout and input

| Project | About |
|---|---|
| **[pane-highlight](https://github.com/olegpulatov/pane-highlight)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `8d` | Marks the active split with a border and tint, dims the others, and recolors a pane by user or host, such as red for `prod-*` hosts. |
| **[tern-ide layout](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/layout.nix)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `1d` | Window plugin with an IDE-style four-pane layout, set split ratios, and an omp pane, packaged with Nix inside a NixOS config. |
| **[tern-plugins (mreishus)](https://github.com/mreishus/tern-plugins)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Collection of small plugins, including one that moves the tab bar to the bottom in the tiles, studio and float layouts and one that opens a pane's scrollback in nvim. |
| **[tern-tab-search](https://github.com/cgasgarth/tern-tab-search)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `10d` | Searches tabs across sessions in a native popup, with `session:tab` filtering and no changes to tab titles or pane layouts. |
| **[tern-close-plugin](https://github.com/yumosx/tern-close-plugin)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `3w` | Adds palette commands that close the other tabs and the split blocks left, right and around the focused block, each row hidden while it would close nothing. |
| **[tern-extrakeys](https://github.com/bneil/tern-extrakeys)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Termux-style bar of buttons for Esc, Ctrl, Alt, Tab, arrows and more that types into a pane you choose, using Termux's extra-keys config format. |
| **[tern-grid-layout](https://github.com/yoyooyooo/tern-grid-layout)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Arranges the panes of a tab into equal-width columns when the window resizes or on request, keeping manual divider changes in between. |

### Integrations

*Plugins that make Tern fit a setup you already work in, such as a multiplexer, editor, window manager or browser.*

| Project | About |
|---|---|
| **[neotern](https://github.com/arg3t/neotern)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 8` `3w` | Neovim drawn as a native Tern surface in the style of Neovide, with a native command palette and picker; alpha and tuned to the author's own dotfiles.<details><summary>Screenshot</summary><img src="https://github.com/arg3t/neotern/raw/main/docs/img/editor.png" width="520" alt="neotern screenshot"></details> |
| **[tern-herdr](https://github.com/safzanpirani/tern-herdr)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 7` `3w` | Shows Herdr as native Tern tabs, splits and a sidebar, with tabs colored by agent state and Herdr's prefix keys working. |
| **[herdr-tern-plugin](https://github.com/gabrielmoreira/herdr-tern-plugin)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Adds an Open Herdr Session command that picks an existing herdr session and attaches to it inside Tern without copying or converting workspaces.<details><summary>Screenshot</summary><img src="https://github.com/gabrielmoreira/herdr-tern-plugin/raw/main/assets/picker.png" width="520" alt="herdr-tern-plugin screenshot"></details> |
| **[Forge Omarchy](https://github.com/Moti-Velz/tern-forge/tree/main/omarchy)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Makes Omarchy's window keys act on Tern panes first and fall through to Hyprland at the edges, in the style of vim-tmux-navigator, with desktop notifications when agents finish or wait for you. |
| **[tern-browser-profiles](https://github.com/ian139/tern-browser-profiles)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Opens a Chrome, Brave or Edge profile on macOS inside Tern as an isolated browser signed in with that profile's cookies. |
| **[tern-vimnav](https://github.com/mayask/tern-vimnav)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `3w` | Brings vim-tmux-navigator to Tern so Ctrl+H/J/K/L moves between Neovim splits and Tern panes. |

### Remote hosts

*Working across machines: connecting to hosts, and moving files, clipboard images and links between local and remote panes.*

| Project | About |
|---|---|
| **[tern-ssh](https://github.com/aancw/tern-ssh)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `3w` | An ssh host manager that runs as a Tern pane. It lists the hosts of an ssh config, connects to them, and adds, edits and removes hosts without leaving Tern.<details><summary>Screenshot</summary><img src="https://github.com/aancw/tern-ssh/raw/main/docs/screenshot.png" width="520" alt="tern-ssh screenshot"></details> |
| **[tern-remote-open](https://github.com/LoneExile/tern-remote-open)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `2w` | Opens file links, localhost URLs and OAuth loopback sign-in links from remote ssh panes on your Mac, where the file or port would not otherwise exist. |
| **[tern-file-paste](https://github.com/vokativ/tern-file-paste)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `10d` | Uploads copied local files from macOS, Linux, and Windows to remote hosts over SSH and inserts their paths into Tern panes. |
| **[remote-image-paste](https://github.com/zyzhou-s-lab/remote-image-paste)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Uploads a macOS clipboard image to the focused remote host over SSH and pastes the server path into the current pane. |
| **[tern-paste-image](https://github.com/Microck/tern-paste-image)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `3w` | Pastes Windows clipboard screenshots into local or remote Tern terminals with Ctrl+Alt+V, uploading over SSH and inserting the quoted path without pressing Enter. |
| **[tern-remote-paste](https://github.com/jmilldotdev/tern-remote-paste)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Makes Ctrl+V in an ssh pane upload a Mac clipboard image to the remote host and paste its path for agents such as omp and Claude Code. |

### Companion apps

*Apps that reach Tern's sessions or agents from outside Tern, on the web, a phone or the desktop.*

| Project | About |
|---|---|
| **[tern-awui](https://github.com/materemias/tern-awui)**<br><a href="#legend"><img src="assets/kinds/companion.svg" alt="companion" align="absmiddle"></a><br>`★ 6` `1d` | Phone and browser web app for the omp agents running in Tern, reached over Tailscale, with sessions grouped by project and two-way control for prompts, questions, model choice, rewind and push notifications.<details><summary>Screenshot</summary><img src="https://github.com/materemias/tern-awui/raw/main/docs/phone.gif" width="520" alt="tern-awui screenshot"></details> |

### Themes and appearance

| Project | About |
|---|---|
| **[omaterm](https://github.com/betizzel/omaterm)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 6` `3w` | Matches Tern's background, foreground, window chrome and ANSI colors to your active Omarchy theme. |
| **[tern-mizu](https://github.com/ITSyndicate25/tern-mizu)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `3w` | Paints the Mizu Icons VS Code file icon theme over the Files pane, with 893 icons covering 847 file names, 947 extensions and 1457 folder names. |
| **[tern-vscode-dark](https://github.com/ITSyndicate25/tern-vscode-dark)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Paints Tern with VS Code's Dark Modern theme, covering window chrome, terminal colors and the file editor's syntax colors. |
| **[font-default](https://github.com/getpipher/font-default)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `3w` | Makes the Reset font size command return to your configured size instead of Tern's built-in default. |
| **[tern-custom-background](https://github.com/naraaalt/tern-custom-background)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Puts a dithered picture behind the whole window, with a settings page to pick the image and how it is drawn. |
| **[tern-kami](https://github.com/justdoswift/tern-kami)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Warm-paper theme with parchment backgrounds, ink-blue accents and serif type, inspired by Kami.<details><summary>Screenshot</summary><img src="https://github.com/justdoswift/tern-kami/raw/feat/tern-kami/assets/preview.png" width="520" alt="tern-kami screenshot"></details> |
| **[tern-omp-layout-fixes](https://github.com/0xGREG/tern-omp-layout-fixes)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `3w` | Widens omp transcripts to the full pane and adds spacing above the composer, touching only omp session surfaces. |
| **[tern-wide-autocomplete](https://github.com/doyouing/tern-wide-autocomplete)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `8d` | Widens omp's native autocomplete menus and lines them up with the composer in Tern's Reader layout. |

### Localization

| Project | About |
|---|---|
| **[tern-zh-cn](https://github.com/maicent/tern-zh-cn)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 5` `2w` | Partial Simplified Chinese translation with Chinese titles for over 50 built-in palette commands and CSS replacement of the palette tabs and tab-bar buttons.<details><summary>Screenshot</summary><img src="https://github.com/maicent/tern-zh-cn/raw/main/docs/screenshot.png" width="520" alt="tern-zh-cn screenshot"></details> |

## Development

*Version control, code review, issues and tasks, and tools for files, infrastructure and data.*

### Git

| Project | About |
|---|---|
| **[tern-jj](https://github.com/resYuto/tern-jj)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Displays `jj status` and `jj st` output as a read-only native card with added, modified and deleted files colored to match the Tern theme. |
| **[tern-jj-diff](https://github.com/zsxawerdu/tern-jj-diff)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `3w` | Renders `jj diff` and `jj show` output as a native view with summary badges and one collapsible section per file, filling the gap left by Tern's built-in `jj st` and `jj log` views. |
| **[TernGitButler](https://github.com/edheltzel/GitButler-for-Tern)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `4d` | GitButler workspaces in Tern, with a status-bar segment, a workspace block with one lane per branch stack and a diff block.<details><summary>Screenshot</summary><img src="https://github.com/edheltzel/GitButler-for-Tern/raw/main/docs/images/demo.gif" width="520" alt="TernGitButler screenshot"></details> |

### Review and feedback

| Project | About |
|---|---|
| **[PR Guide](https://github.com/jubbydev/tern-pr-guide)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 6` `5d` | Walks through a GitHub pull request one change at a time with the code beside a plain explanation, then lets you comment and post a single review.<details><summary>Screenshot</summary><img src="https://github.com/jubbydev/tern-pr-guide/raw/main/docs/screenshots/hub.png" width="520" alt="PR Guide screenshot"></details> |
| **[tern-margin](https://github.com/Noctivoro/tern-margin)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 3` `3w` | Renders a Markdown file block by block so you can leave CriticMarkup comments on any paragraph, list, table or code block, and hands them back to the agent that opened it.<details><summary>Screenshot</summary><img src="https://github.com/Noctivoro/tern-margin/raw/main/docs/screenshot.png" width="520" alt="tern-margin screenshot"></details> |
| **[tern-annotate](https://github.com/hyper-stition/tern-annotate)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Prototype for commenting on a snapshot of any block and sending the edit comments to an agent in batches. |
| **[Tern Reviewr](https://github.com/AxelMrak/tern-reviewr)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Reviews staged, unstaged, and untracked Git changes in a native Tern diff view, sends line-anchored comments directly to an agent, and tracks per-file review progress. |
| **[tern-difftastic](https://github.com/MicroProofs/tern-difftastic)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `11d` | Reviews jj and git changes as difftastic's structural side-by-side diffs in a block, with search across both sides of every file and seen and reviewed marks on hunks that survive rebases.<details><summary>Screenshot</summary><img src="https://github.com/MicroProofs/tern-difftastic/raw/main/docs/screenshot.png" width="520" alt="tern-difftastic screenshot"></details> |
| **[tern-pr-tour](https://github.com/lfsmoura/tern-pr-tour)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `4d` | Step-by-step tours of a pull request that can answer questions inline, with a matching pr-tour agent skill.<details><summary>Screenshot</summary><img src="https://github.com/lfsmoura/tern-pr-tour/raw/main/docs/step.png" width="520" alt="tern-pr-tour screenshot"></details> |

### Issues and tasks

| Project | About |
|---|---|
| **[tern-todo](https://github.com/deLiseLINO/tern-todo)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `2w` | Task manager with tasks linked to terminal panes and agent sessions, kept in a JSON file and installable on remote hosts.<details><summary>Screenshot</summary><img src="https://raw.githubusercontent.com/deLiseLINO/tern-todo/341b91aa29ca420e63a285d29772d490217e2672/shots/tasks-dark.png" width="520" alt="tern-todo screenshot"></details> |
| **[tern-kata](https://github.com/Dangerboi/tern-kata)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 2` `5d` | Browses and edits kata issues in a native pane opened with F9 or the palette, with Markdown issue bodies, priority and label chips, and kata links from agent chat that open the issue.<details><summary>Screenshot</summary><img src="https://github.com/Dangerboi/tern-kata/raw/main/docs/images/tern-kata.png" width="520" alt="tern-kata screenshot"></details> |
| **[tern-tracker](https://github.com/foxzool/tern-tracker)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Lists the GitHub issues and pull requests of the repository in the focused pane's directory, with comments and a form for creating issues, in English or Chinese. |
| **[jira-tern](https://github.com/hanbong5938/jira-tern)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Native Jira browser that reads and posts issue comments, runs status transitions, and opens a Git worktree or jj workspace with an omp agent tab for an issue. |

### File viewers and notebooks

| Project | About |
|---|---|
| **[tern-pencil-preview](https://github.com/SamuelFontess/tern-pencil-preview)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 7` `4d` | Previews pen.dev (Pencil) `.pen` designs in a block, rendering every top-level frame in one pen CLI run into a disk cache so switching frames is instant, with a layer list, an inspector and re-renders on save.<details><summary>Screenshot</summary><img src="https://github.com/SamuelFontess/tern-pencil-preview/raw/main/docs/editor.png" width="520" alt="tern-pencil-preview screenshot"></details> |
| **[tern-office-preview](https://github.com/zerx-lab/tern-office-preview)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Previews Word and Excel files natively in a block using a Rust renderer, with no Office, browser or LibreOffice involved.<details><summary>Screenshot</summary><img src="https://github.com/zerx-lab/tern-office-preview/raw/main/assets/xlsx.png" width="520" alt="tern-office-preview screenshot"></details> |
| **[tern-video-block](https://github.com/verticalrectangle/tern-video-block)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Opens video files in a block with mpv sound, frame stepping and synced side-by-side playback using ffmpeg and the kitty graphics protocol. |
| **[tern-obsidian](https://github.com/dbydd/tern-obsidian)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `1d` | Recognizes Obsidian vaults and opens their notes, Bases and JSON Canvas files in native reader blocks. |
| **[tern-canvas-viewer](https://github.com/iacore/tern-canvas-viewer)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Opens `.excalidraw` and `.tldraw` drawings as a rendered picture in a block instead of their JSON source.<details><summary>Screenshot</summary><img src="https://github.com/iacore/tern-canvas-viewer/raw/main/docs/preview.png" width="520" alt="tern-canvas-viewer screenshot"></details> |
| **[tern-csv](https://github.com/taooceros/tern-csv)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Shows CSV and TSV files as a native keyboard-driven table with a Table and Text switch.<details><summary>Screenshot</summary><img src="https://github.com/taooceros/tern-csv/raw/main/docs/switch-table.png" width="520" alt="tern-csv screenshot"></details> |
| **[tern-rmd](https://github.com/betizzel/tern-rmd)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Opens R Markdown files as notebooks, running chunks in one live R session with plots and paged data frames shown under each chunk.<details><summary>Screenshot</summary><img src="https://github.com/betizzel/tern-rmd/raw/main/docs/screenshot.png" width="520" alt="tern-rmd screenshot"></details> |
| **[kedi-tern](https://github.com/kedi-lang/kedi-tern)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `3w` | Read-only viewer for `.kedi` files that highlights them in a native Tern editor using tree-sitter, without running the embedded Python. |

### Cloud and data

| Project | About |
|---|---|
| **[tern-grafana](https://github.com/contrafy/tern-grafana)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 7` `11d` | Grafana and Prometheus-compatible backends as native blocks for PromQL queries, dashboards, alerts and silences, logs and traces; pre-release.<details><summary>Screenshot</summary><img src="https://github.com/contrafy/tern-grafana/raw/master/docs/screenshots/dashboard.png" width="520" alt="tern-grafana screenshot"></details> |
| **[tern-kube](https://github.com/contrafy/tern-kube)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 7` `1d` | Renders `kubectl` output as sortable, filterable native views, with a live Explore block, one-key pod shells and logs, previewed and confirmed changes, and GitOps drift against your manifests.<details><summary>Screenshot</summary><img src="https://github.com/contrafy/tern-kube/raw/master/docs/screenshots/m1-inspector-dark-wide.png" width="520" alt="tern-kube screenshot"></details> |
| **[tern-netsuite](https://github.com/contrafy/tern-netsuite)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `4d` | Native views for the NetSuite SuiteCloud SDF CLI with a production deploy guard, a project explorer and read-only SuiteQL execution logs and account health; public beta.<details><summary>Screenshot</summary><img src="https://github.com/contrafy/tern-netsuite/raw/master/docs/screenshots/lens-validate.png" width="520" alt="tern-netsuite screenshot"></details> |
| **[tern-bigquery](https://github.com/junaidrahim/tern-bigquery)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | BigQuery browser built on the `bq` tool, with project search, dataset and table navigation, schema inspection and scrollable data previews. |

### System and developer tools

| Project | About |
|---|---|
| **[rmon](https://github.com/pgkt04/rmon)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 10` `13d` | Resource monitor for Linux and macOS with CPU, GPU, memory, network, disk and process panels and a disk benchmark, drawn natively in Tern over TSP.<details><summary>Screenshot</summary><img src="https://github.com/pgkt04/rmon/raw/main/media/demo.png" width="520" alt="rmon screenshot"></details> |
| **[mantern](https://github.com/theblazehen/mantern)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 6` `3w` | Drop-in `man` replacement that draws pages natively in Tern over TSP, with a synopsis card, option cards, tables, foldable sections and clickable SEE ALSO links, and falls back to the system `man` elsewhere.<details><summary>Screenshot</summary><img src="https://github.com/theblazehen/mantern/raw/main/docs/screenshot.png" width="520" alt="mantern screenshot"></details> |
| **[tern-clock](https://github.com/ajaxdude/tern-clock)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `11d` | Live system clock in the tab bar, in 12- or 24-hour format with optional seconds and a choice of four positions. |
| **[tern-find-in-files](https://github.com/jmilldotdev/tern-find-in-files)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | VS Code-style search across the files under a folder, powered by ripgrep, with results updating as you type. |
| **[tern-ports](https://github.com/meisijiya/tern-ports)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `6d` | Shows every listening TCP port on your machine and marks the ones an omp process started.<details><summary>Screenshot</summary><img src="https://github.com/meisijiya/tern-ports/raw/master/docs/ports.png" width="520" alt="tern-ports screenshot"></details> |
| **[tern-status](https://github.com/getpipher/tern-status)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `3w` | Status line in the style of tmux with CPU, memory, battery, network, disk and clock segments drawn with Tern's own icons and theme tones. |
| **[tern-commands](https://github.com/lucaxic/tern-commands)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2d` | Turns the code blocks in a `COMMANDS.md` file into grouped command buttons.<details><summary>Screenshot</summary><img src="https://github.com/lucaxic/tern-commands/raw/main/assets/screenshot.png" width="520" alt="tern-commands screenshot"></details> |
| **[tern-dbgview](https://github.com/Hime7864/tern-dbgview)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Shows Windows debug output as it is produced, from kernel-mode `DbgPrint` and user-mode `OutputDebugString`. |
| **[tern-jobs](https://github.com/eggpeat/tern-jobs)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `8d` | Lists your systemd user timers and failed user services in a block with each job's last result and next run, shows the journal of its last run, starts a job on a double `s` press and toasts when a job fails or recovers. |
| **[tern-nom](https://github.com/tdortman/tern-plugins/tree/main/crates/nom)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 0` `1d` | Shows nix-output-monitor as a live native card with builds, downloads, flake updates and nh's closure diff, and runs the plain program outside Tern. |

## Media and fun

*Music, games, toys, and whatever doesn't fit anywhere else.*

### Music and media

| Project | About |
|---|---|
| **[tern-spotify](https://github.com/rico-vz/tern-spotify)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `3w` | Player block for the Spotify desktop app with cover art, playback, seeking and volume controls on macOS, Windows and Linux.<details><summary>Screenshot</summary><img src="https://github.com/rico-vz/tern-spotify/raw/main/assets/preview-pip.png" width="520" alt="tern-spotify screenshot"></details> |
| **[tern-spotify (Windows)](https://github.com/NaC-L/tern-spotify)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 4` `3w` | Floating player for the Windows Spotify desktop app with cover art, playback controls, search, keyboard shortcuts and the current track in the status line.<details><summary>Screenshot</summary><img src="https://github.com/NaC-L/tern-spotify/raw/main/docs/tern-spotify-demo.gif" width="520" alt="tern-spotify (Windows) screenshot"></details> |
| **[tern-CDP-tidal](https://github.com/H4vC/tern-CDP-tidal)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Player block for the TIDAL desktop app, driven over the Chrome DevTools protocol, with cover art, playback, seeking, volume, shuffle, repeat and line-based search. |
| **[tern-spotify (kyle-elliott)](https://github.com/kyle-elliott/tern-spotify)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `3w` | Spotify player pane with album art, queue, library, search and device picker, plus a floating mode, status-line track and palette commands for playback. |
| **[Warble](https://github.com/ElkinAMG/tern-warble)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `9d` | Spotify player block that controls any Spotify Connect device through the Web API, with cover art, seeking, volume, shuffle, repeat, a device picker and search; macOS only for now.<details><summary>Screenshot</summary><img src="https://github.com/ElkinAMG/tern-warble/raw/main/docs/screenshots/player-docked-dark.png" width="520" alt="Warble screenshot"></details> |
| **[tern-spotify (taooceros)](https://github.com/taooceros/tern-spotify)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `8d` | Spotify player backed by a librespot daemon that shows up as a Connect device, with your library, album pages and synced lyrics; needs Spotify Premium.<details><summary>Screenshot</summary><img src="https://github.com/taooceros/tern-spotify/raw/main/docs/player.png" width="520" alt="tern-spotify (taooceros) screenshot"></details> |

### Fun

| Project | About |
|---|---|
| **[tern-cat](https://github.com/contrafy/tern-cat)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 7` `2w` | Adds a pixel-art menace that naps in your panes, swats at your pointer, stares when you sudo and dives through portals when you switch panes.<details><summary>Screenshot</summary><img src="https://github.com/contrafy/tern-cat/raw/master/docs/images/overlay-cat.png" width="520" alt="tern-cat screenshot"></details> |
| **[Ternatro](https://github.com/verusferro/Ternatro)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 4` `3w` | Plays Balatro in a Tern pane, running the game's own Lua code from your copy of Balatro.exe and drawing its layout, card motion, particles and shaders natively; you need to own the game. |
| **[tern-pokemon](https://github.com/ITSyndicate25/tern-pokemon)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Ports vscode-pokemon to a block where Pokémon walk, sit and get petted on themed beach, forest and castle scenes, drawn natively with animated GIF sprites and no web view. |
| **[Toons](https://github.com/TazeDiB/Toons-Tern)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 3` `3w` | Draws cartoons of what the agent is doing while commands run, as a port of claude-toons to Tern's native UI. |
| **[tern-git-fx](https://github.com/willstarnet/tern-git-fx)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Plays a small pixel-art animation in the pane corner while a git command runs, then a success or failure ending based on its exit status.<details><summary>Screenshot</summary><img src="https://github.com/willstarnet/tern-git-fx/raw/main/docs/images/sprites-preview.png" width="520" alt="tern-git-fx screenshot"></details> |
| **[TernMeOn](https://github.com/segmentationf4u1t/Tern-Me-On)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Controls Buttplug devices from Tern, with haptic patterns written as code and feedback when long commands finish.<details><summary>Screenshot</summary><img src="https://github.com/segmentationf4u1t/Tern-Me-On/raw/main/docs/devices.png" width="520" alt="TernMeOn screenshot"></details> |
| **[power-surge](https://github.com/dbydd/power-surge)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Neovim plugin that shows sparks on every text change with a combo meter and screen shake, with a Tern command and chord for it. |

### Other

*Plugins and apps that don't fit another section yet.*

| Project | About |
|---|---|
| **[Terngram](https://github.com/d3d0n/terngram)**<br><a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a><br>`★ 4` `3w` | Unofficial keyboard-driven Telegram client built on TDLib and omp's UI toolkit, also installable as a Tern plugin. |
| **[tern-pomodoro](https://github.com/tcstacks/tern-pomodoro)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `3w` | Minimal timer block with 25-minute focus and 5-minute break defaults, adjustable durations and a quiet progress line, using no network or subprocesses.<details><summary>Screenshot</summary><img src="https://github.com/tcstacks/tern-pomodoro/raw/main/assets/preview.png" width="520" alt="tern-pomodoro screenshot"></details> |
| **[tern-rss](https://github.com/bmanturner/tern-rss)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 2` `2w` | Follows RSS and Atom feeds in a block with expandable previews, articles in a docked reader browser, toasts for starred feeds and a catch-up line instead of an ever-growing unread count.<details><summary>Screenshot</summary><img src="https://github.com/bmanturner/tern-rss/raw/main/docs/latest.png" width="520" alt="tern-rss screenshot"></details> |
| **[Carly Switch](https://github.com/zyzhou-s-lab/carly-switch)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 1` `2w` | Switches Carly's native realtime voice between Doubao and OpenAI from a compact panel, including a connection test that does not start the microphone. |
| **[Forge Meetings](https://github.com/Moti-Velz/tern-forge/tree/main/meetings)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Lists Granola and Fireflies meetings, email threads over IMAP and local transcript exports in one keyboard-driven block, and pastes the ones you pick into the agent's composer as a summary or full transcript.<details><summary>Screenshot</summary><img src="https://github.com/Moti-Velz/tern-forge/raw/main/meetings/docs/screenshot.png" width="520" alt="Forge Meetings screenshot"></details> |

## Building for Tern

*Documentation, SDKs and starting points for writing your own Tern plugins and apps.*

### Documentation

| Project | About |
|---|---|
| **[Tern plugin book](https://docs.stencil.so/tern/)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Official documentation covering host and window runtimes, lenses, blocks, native views, styling, and TSP. |
| **[Getting Started](https://docs.stencil.so/tern/guides/getting-started.html)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Walkthrough of building a lens and palette command, then linking, type-checking, and reloading. |
| **[Command Lenses](https://docs.stencil.so/tern/guides/lenses.html)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Explains how to turn command output into native views using manifest globs and host callbacks. |
| **[Debugging](https://docs.stencil.so/tern/guides/debugging.html)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Covers toasts, logs, Luau typing, handler budgets, and scripted window control. |
| **[Plugin CLI](https://docs.stencil.so/tern/reference/cli.html)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Reference for `tern plugin list`, `install`, `link`, `unlink`, `remove`, `reload`, `dir`, and `types`. |
| **[Tern Surface Protocol](https://docs.stencil.so/tern/protocol/index.html)**<br><a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Specifies the in-band protocol where CLIs, TUIs, and agents send UI trees that Tern lays out and draws natively. |

### SDKs and protocol libraries

| Project | About |
|---|---|
| **[tern-sdk](https://github.com/stencil-hq/tern-sdk)**<br><a href="#legend"><img src="assets/kinds/library.svg" alt="library" align="absmiddle"></a><br>`★ 96` `2d` | Official repository of Surface Protocol SDKs for Rust, Python, Go and TypeScript, plus the Luau type definitions (`tern.d.luau`) and example plugins. |
| **[@oh-my-pi/pi-wire](https://github.com/can1357/oh-my-pi/tree/main/packages/wire)**<br><a href="#legend"><img src="assets/kinds/library.svg" alt="library" align="absmiddle"></a><br>`★ 37.3k` `today` | TypeScript package implementing the TSP wire format: APC framing, component types, frame operations, handshake and events. |
| **[@oh-my-pi/pi-tui](https://github.com/can1357/oh-my-pi/tree/main/packages/tui)**<br><a href="#legend"><img src="assets/kinds/library.svg" alt="library" align="absmiddle"></a><br>`★ 37.3k` `today` | TypeScript UI toolkit from omp for rendering transcripts, chat, dashboards, and pickers natively over TSP. |
| **[octet-tern](https://github.com/skaft-software/octet/tree/9e8abda1f4f210d43361b6c0a80e482097feff77/crates/octet-tern)**<br><a href="#legend"><img src="assets/kinds/library.svg" alt="library" align="absmiddle"></a><br>`★ 10` `1d` | A Rust TSP client built into Octet with wire types, APC chunking, tty flow control, and scene builders. |

### Plugin templates and tooling

| Project | About |
|---|---|
| **[tern-plugin-base](https://github.com/olegpulatov/tern-plugin-base)**<br><a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a><br>`★ 0` `2w` | Minimal starting point for a Tern plugin to copy, with package, config and dev commands and an example that logs a greeting on load. |

## Packaging and dotfiles

*Tern builds are behind a sign-in, so these Nix setups expect you to download the build yourself.*

| Project | About |
|---|---|
| **[pelikanade/flake](https://github.com/pelikanade/flake/blob/f6f8217278a4a119c8e3a5b27b5a30ffef57cbd1/docs/tern.md)**<br><a href="#legend"><img src="assets/kinds/config.svg" alt="config" align="absmiddle"></a><br>`★ 11` `1d` | Nix packaging guide covering signed-in downloads, `requireFile`, graphics libraries, and updating. |
| **[plumj-am/nixos](https://github.com/plumj-am/nixos/blob/master/modules/tern.nix)**<br><a href="#legend"><img src="assets/kinds/config.svg" alt="config" align="absmiddle"></a><br>`★ 3` `1d` | NixOS module that manages Tern settings, theme, tmux-style keybindings, the `omp` launch command and plugins. |
| **[tdortman/dotfiles](https://github.com/tdortman/dotfiles/tree/008242f1f3ef305950a98f9878a0253477f256b0/nix)**<br><a href="#legend"><img src="assets/kinds/config.svg" alt="config" align="absmiddle"></a><br>`★ 1` `3d` | A Nix package with desktop entries, an update script finding new builds via a Stencil browser session, and a KDE Plasma Home Manager module where Meta+Return focuses Tern or starts it. |
| **[theoparis/nix-tern](https://github.com/theoparis/nix-tern)**<br><a href="#legend"><img src="assets/kinds/config.svg" alt="config" align="absmiddle"></a><br>`★ 1` `11d` | Nix flake that packages a hand-downloaded Tern tarball and keeps it from being garbage collected. |

## Legend

| Label | Meaning |
|---|---|
| <a href="#legend"><img src="assets/kinds/plugin.svg" alt="plugin" align="absmiddle"></a> | Luau plugin |
| <a href="#legend"><img src="assets/kinds/app.svg" alt="app" align="absmiddle"></a> | App drawn natively over TSP |
| <a href="#legend"><img src="assets/kinds/extension.svg" alt="extension" align="absmiddle"></a> | Runs inside your coding agent |
| <a href="#legend"><img src="assets/kinds/companion.svg" alt="companion" align="absmiddle"></a> | Runs outside Tern |
| <a href="#legend"><img src="assets/kinds/library.svg" alt="library" align="absmiddle"></a> | SDK or protocol library |
| <a href="#legend"><img src="assets/kinds/config.svg" alt="config" align="absmiddle"></a> | Nix package or dotfiles |
| <a href="#legend"><img src="assets/kinds/docs.svg" alt="docs" align="absmiddle"></a> | Documentation |
| `★ 36.4k` `3d` | GitHub stars and time since the last push |
| `inactive` `archived` `unavailable` | No push in six months, archived, or the repository is gone |

## Contributing

Suggestions are welcome as pull requests. Read the [contribution guidelines](CONTRIBUTING.md) first.
