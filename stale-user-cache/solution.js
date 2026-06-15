/**
 * Fixed approach — invalidate cached profile data after a username write.
 *
 * Step-by-step:
 * 1) Read user profile through cache-aside (Redis, then database).
 * 2) Update username in the database.
 * 3) Delete the stale cache key so the next read loads fresh data.
 */

// userController.js

async function updateUsername(userId, username) {
  const user = await db.users.findById(userId);

  user.username = username;

  await db.users.save(user);

  // Step 3: drop cached profile so getProfile cannot return old username.
  await redis.del(`user:${userId}`);

  return user;
}

// profileController.js

async function getProfile(userId) {
  const cached = await redis.get(`user:${userId}`);

  if (cached) {
    return JSON.parse(cached);
  }

  const user = await db.users.findById(userId);

  // Step 1: cache fresh profile for subsequent reads.
  await redis.set(`user:${userId}`, JSON.stringify(user), "EX", 3600);

  return user;
}

module.exports = { updateUsername, getProfile };
