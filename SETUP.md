# Kya kya karna hai

1. ZIP extract karo. `harir03/harir03` already exists, so preserve its history. Terminal / PowerShell mein:

   ```bash
   git clone https://github.com/harir03/harir03.git hari-profile
   cd hari-profile
   ```

   Copy **everything inside the ZIP's `harir03` folder** into `hari-profile`, overwriting matching files. Include hidden `.github`, `.gitattributes` and `.gitignore`. Do not copy the outer `harir03` folder as a nested folder. Do not delete `.git`. If you already have a clean local clone, use it instead.

2. Open `preview.html` and review `README.md`. The skill map is unranked: all included areas have the same presence marker, not fake proficiency scores. Edit `assets/skills.json` only if you want your own ratings. The avatar portrait, stats, radars, repo cards, isometric calendar and Invaders are already generated. Invaders is an animation, not a keyboard-playable game.

3. Push, without force:

   ```bash
   git status
   git add README.md SETUP.md SOURCE-NOTICE.md requirements.txt setup.ps1 preview.html .github .gitattributes .gitignore scripts assets
   git commit -m "feat: full profile with generated portrait, charts and arcade"
   git push origin main
   ```

   If the push says someone updated the remote, run `git pull --rebase origin main`, resolve any real conflicts, then push. Do not use `--force`. Keep the profile repository public. `SOURCE-NOTICE.md` explains the upstream's missing license; get permission from its author before public reuse of its code/design.

4. In the repo, go to **Settings > Actions > General > Workflow permissions > Read and write permissions > Save**. The workflow files also request `contents: write`. If GitHub Actions is disabled, enable it. Branch rules blocking direct bot commits need an explicit exception or a PR-based workflow.

5. Full optional metrics ke liye a PAT add karo. GitHub **Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token (classic)**. Use a sensible expiry. For these public metrics, upstream documents a **scopeless token** as enough by default. Optional `read:user` / `read:org` / `read:packages` scopes unlock related extra badges. Do **not** add `repo` unless you intentionally want private-repository access. The commit uses GitHub's separate built-in token, so the PAT does not need repo write permission for this setup.

   Copy the token directly into your profile repo's **Settings > Secrets and variables > Actions > New repository secret**. Name it exactly `METRICS_TOKEN`. Don't put it in README, code, a screenshot or chat. You do not create a `GITHUB_TOKEN` secret: GitHub supplies it automatically.

6. **Actions > Charts and cards > Run workflow > main > Run workflow**. Then **Actions > Metrics > Run workflow > main > Run workflow**. Wait for both to finish; pull the bot's commits if you keep a local clone:

   ```bash
   git pull --rebase origin main
   ```

   Charts runs daily at 03:30 UTC (09:00 IST), on relevant file pushes and manually. Metrics runs every 6 hours and manually. GitHub can delay scheduled jobs, and disables scheduled workflows after 60 days of inactivity in public repositories. Without `METRICS_TOKEN`, Metrics deliberately skips its three generators: habits and achievements retain setup notices, and languages retains the initial public-byte snapshot. The rest works with GitHub's automatic token and public contribution HTML.

## Optional: regenerate locally

Python 3.12 is used in Actions. On Windows use `py` if `python` is not available.

```bash
python -m pip install -r requirements.txt
python scripts/dotify.py assets/avatar.png -o assets/portrait --cols 100 --equalize --detail 0.5 --color --reveal --bg "#0d1117"
python scripts/radar.py --data assets/skills.json -o assets/radar
python scripts/radar.py --github harir03 -o assets/radar-langs --limit 7 --values --curve 0.4 --exclude "shell,makefile,dockerfile,batchfile,procfile"
python scripts/cards.py --user harir03 --projects assets/projects.json --out assets
python scripts/isocalendar.py --user harir03 --config assets/calendar.json -o assets/metrics.isocalendar.svg
python scripts/invaders.py --user harir03 --config assets/invaders.json -o assets/invaders.svg
```

`setup.ps1` is a Windows helper; install Pillow first. Public GitHub API calls can hit anonymous rate limits locally. Actions supplies its built-in token. A token is not needed for the portrait or manual skill map.

The isometric calendar uses actual contribution days. Its labels say contributions/streaks, not exclusively commits. The language radar is normalized with a power curve, not literal percentages or a proficiency test. Config `calendar.json` controls calendar animation and palette; keep streak overrides null for truthful stats. `invaders.json` currently controls the username only; decorative options from upstream are not implemented by its renderer.

## Token reference

- Upstream Metrics token and separate committer token: https://github.com/lowlighter/metrics/blob/master/source/plugins/core/README.md
- Habits plugin: https://github.com/lowlighter/metrics/blob/master/source/plugins/habits/README.md
- Languages plugin: https://github.com/lowlighter/metrics/blob/master/source/plugins/languages/README.md
- Achievements plugin: https://github.com/lowlighter/metrics/blob/master/source/plugins/achievements/README.md
