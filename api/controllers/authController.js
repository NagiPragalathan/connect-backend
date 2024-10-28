const User = require('../models/User');
const jwt = require('jsonwebtoken');

const { generateAccessToken, generateRefreshToken, hashPassword, comparePassword } = require('../services/authService');

exports.signup = async (req, res) => {
    const { username, password } = req.body;
    try {
        const existingUser = await User.findOne({ username });
        if (existingUser) {
            return res.status(400).json({ message: "Username already exists" });
        }

        const newUser = new User({
            username,
            password: hashPassword(password)
        });
        await newUser.save();

        const accessToken = generateAccessToken(newUser._id, newUser.username);
        const refreshToken = generateRefreshToken(newUser._id, newUser.username);

        res.status(201).json({ message: "User registered successfully", accessToken, refreshToken });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Internal server error" });
    }
};

exports.login = async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (!user || !comparePassword(password, user.password)) {
            return res.status(400).json({ message: 'Invalid username or password' });
        }

        const accessToken = generateAccessToken(user._id, user.username);
        const refreshToken = generateRefreshToken(user._id, user.username);

        res.json({ accessToken, refreshToken });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Internal server error" });
    }
};

exports.refreshToken = (req, res) => {
    const { refreshToken } = req.body;
    if (!refreshToken) return res.status(403).json({ message: 'No refresh token provided' });

    jwt.verify(refreshToken, process.env.REFRESH_SECRET_KEY, (err, user) => {
        if (err) return res.status(403).json({ message: 'Invalid refresh token' });

        const newAccessToken = generateAccessToken(user.id, user.username);
        res.json({ accessToken: newAccessToken });
    });
};
