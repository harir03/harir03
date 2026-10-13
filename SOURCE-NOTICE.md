# Source and reuse notice

Scaffolding source: https://github.com/Programmer-NITIN/Programmer-NITIN

Inspected commit: `2df5302a18606c0bb15e44ace7794650e5b40c54`.

The source tree contained no LICENSE file or explicit license grant at inspection on 2026-10-13. Public GitHub visibility is not an open-source reuse license. This is a private adaptation supplied for review. Attribution alone does not grant permission. Ask the upstream author for permission before publicly publishing copied code/design; do not add an MIT license to material you do not own.

Copied/adapted: the five upstream Python generators, the Metrics and Charts and cards workflows, calendar/Invaders config files, preview template, PowerShell helper, .gitignore and .gitattributes. The workflow and script defaults target harir03. Added `contributions.py` to validate exact public counts and reject missing data. Invaders targets are selected from actual active days instead of Nitin's fixed coordinates. Added workflow concurrency and portrait regeneration. Fixed player name, HUD overlap and calendar wording.

Freshly generated for harir03: public avatar dot portrait, dark/light skill map, live dark/light language radars, dark/light statistics card, dark/light cards for altgrade-aws, aria and micro.ai, animated isometric calendar and Invaders. No generated Nitin images or profile numbers were retained. `assets/avatar.png` was retrieved from https://github.com/harir03.png. `assets/snapshot.json` records initial public contribution/language data; it contains no credentials.

Initial language breakdown is a locally generated public-repository-byte snapshot. Habits and GitHub achievements are honest setup-notice SVGs, not fabricated metrics. The Metrics workflow replaces all three after METRICS_TOKEN is configured. The base README came from the supplied adaptation, with original generated sections restored and B.Tech corrected to B.E. based on the profile context.

The upstream has no separate playable game code. Space Invaders is a looping animated SVG and works inside an image. Its cosmetic config fields are currently ignored by upstream code; only username is read. Skill values are unranked presence markers, not claimed self-ratings.

Dependencies/actions retain their own licenses. Python generators need only stdlib except dotify.py, which needs Pillow. Lowlighter Metrics is an external action, currently retained at the upstream's `@latest` reference. Review third-party actions before adding secrets; pin a reviewed immutable commit for stricter supply-chain control.
