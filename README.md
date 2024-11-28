# Virtual Aquarium 🐠🌊

An interactive virtual aquarium simulation where users can create and maintain their own underwater ecosystem.

## Features

- 🐟 Multiple species of fish with unique behaviors
- 🌿 Various aquatic plants and decorations
- 🌡️ Real-time water parameter simulation (pH, temperature, etc.)
- 🍽️ Feeding and care system
- 📈 Fish growth and breeding mechanics
- 🎮 Interactive elements and animations

## Technical Stack
- Backend: Python/Flask
- Frontend: HTML5, CSS3, JavaScript
- Database: SQLite
- Animation: Three.js for 3D rendering
- Real-time Updates: WebSocket

## Project Structure
```
/VirtualAquarium
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── static/            # Static assets
│   ├── css/          # Stylesheets
│   ├── js/           # JavaScript files
│   ├── models/       # 3D models
│   └── images/       # Images and textures
├── templates/         # HTML templates
└── instance/          # Instance-specific files
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
```

4. Initialize the database:
```bash
python app.py
```

5. Access the application:
- Open your browser and go to `http://localhost:5000`
- Create your aquarium
- Start adding fish and decorations!

## Aquarium Features

### Fish Species
- Tropical Fish
  - Guppies
  - Tetras
  - Angelfish
- Cold Water Fish
  - Goldfish
  - Koi
- Marine Fish
  - Clownfish
  - Royal Tang
  - Butterfly Fish

### Environment Features
- Temperature Control
- Lighting System
- Water Quality Monitoring
- Feeding Schedule
- Disease Management
- Ecosystem Balance

### Decorations
- Plants
  - Aquatic Plants
  - Coral Reefs
- Structures
  - Rocks
  - Driftwood
  - Castles
  - Shipwrecks

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Guidelines
- Follow PEP 8 style guide for Python code
- Use meaningful commit messages
- Add comments for complex logic
- Update documentation for new features

## Future Enhancements
- [ ] VR support
- [ ] Community features
- [ ] Advanced fish AI behaviors
- [ ] Real-time fish interaction
- [ ] Mobile app support

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- GitHub: [@KisnaIsOP](https://github.com/KisnaIsOP)
- Project Link: [https://github.com/KisnaIsOP/VirtualAquarium](https://github.com/KisnaIsOP/VirtualAquarium)
