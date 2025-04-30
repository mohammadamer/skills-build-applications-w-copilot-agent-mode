// Select the database (assumes 'db' is already connected to your MongoDB instance)
const db = db.getSiblingDB("octofit_db");
db.createCollection("users");
db.createCollection("teams");
db.createCollection("activity");
db.createCollection("leaderboard");
db.createCollection("workouts");
db.users.createIndex({ "email": 1 }, { unique: true });
db.teams.createIndex({ "name": 1 }, { unique: true });
db.activity.createIndex({ "activity_id": 1 }, { unique: true });
db.leaderboard.createIndex({ "leaderboard_id": 1 }, { unique: true });
db.workouts.createIndex({ "workout_id": 1 }, { unique: true });
