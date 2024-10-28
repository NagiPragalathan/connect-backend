// config/db.js
const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect("mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/connect-backend");
        console.log('MongoDB connected');
    } catch (error) {
        console.error('Error connecting to MongoDB', error);
        process.exit(1);  // Exit the process with failure
    }
};

module.exports = connectDB;
