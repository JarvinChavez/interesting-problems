# Stale user cache after username update

## Problem report

> "I changed my username but other pages still show my old username."

Two controllers share the same user record:

- `updateUsername` writes the new username to the database.
- `getProfile` serves profile data through Redis (`user:{userId}`, 1-hour TTL).

## What went wrong (`attempt.js`)

The write path updates the database only. The read path can still return a **cached profile** created before the username change, so other pages keep showing the old value until the cache entry expires.

This is a **cache invalidation** gap between write and read.

## Step-by-step solution notes

1. **Identify shared cache key:** profile reads use `user:${userId}`.
2. **Keep cache-aside on read:** check Redis first; on miss, load from DB and set TTL.
3. **Invalidate on write:** after saving the new username, delete `user:${userId}` from Redis.
4. **Next profile request:** cache miss → fresh DB row → updated username returned.

See `solution.js` — the only change on the write path is:

```javascript
await redis.del(`user:${userId}`);
```

## Alternative (not used here)

Write-through: update Redis with the new user object immediately after save. Deleting the key is the smallest change and keeps read logic unchanged.

## Files

| File | Purpose |
|------|---------|
| [attempt.js](attempt.js) | Original controllers — DB update without cache sync |
| [solution.js](solution.js) | Same structure with cache invalidation on username update |
