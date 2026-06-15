/**
 * Incomplete attempt — username updates persist to the database but cached
 * profile responses can still return the previous username until TTL expires.
 */

// userController.js

async function updateUsername(userId, username) {
  const user = await db.users.findById(userId);

  user.username = username;

  await db.users.save(user);

  return user;
}

// profileController.js

async function getProfile(userId) {
  const cached = await redis.get(`user:${userId}`);

  if (cached) {
    return JSON.parse(cached);
  }

  const user = await db.users.findById(userId);

  await redis.set(`user:${userId}`, JSON.stringify(user), "EX", 3600);

  return user;
}

module.exports = { updateUsername, getProfile };
