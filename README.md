# Zen Matcha Guide — Pinterest Auto-Poster

Automatically posts one Pinterest pin per day, cycling through 12 blog articles.

## Setup

1. Create a Pinterest Developer App at https://developers.pinterest.com
2. Get an access token with `boards:read`, `boards:write`, `pins:read`, `pins:write` scopes
3. Add the token as a GitHub Secret: `PINTEREST_ACCESS_TOKEN`
4. The workflow runs daily at 15:00 UTC (midnight JST)

## Manual Run

Go to Actions → "Daily Pinterest Pin" → "Run workflow" to post a pin manually.
