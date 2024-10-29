const express = require('express');
const router = express.Router();
const { uploadUserPhoto, getUserPhotoByUsername1, getConnectionsByUsername } = require('../controllers/userPhotoController');
const multer = require('multer');

const upload = multer({ storage: multer.memoryStorage() });

router.post('/upload', upload.single('photo'), uploadUserPhoto);
router.get('/:username_1', getUserPhotoByUsername1);
router.get('/connections/:username', getConnectionsByUsername);

module.exports = router;