# Game Management System

The Game Management System (GMS) is a Python-based application designed to manage and organize games, track player scores, and maintain leaderboards.

## Features

- **Game Management**: Add, update, and delete games from the system.
- **Player Score Tracking**: Record and update player scores for each game.
- **Leaderboard Maintenance**: Automatically update and display leaderboards based on player scores.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HaykuhiMk/Game-Management-System.git
   cd Game-Management-System
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   python main.py
   ```

2. **Interacting with the System**:

   - Follow the on-screen prompts to add games, record player scores, and view the leaderboard.
   - Data is stored in JSON format for simplicity and ease of access.

## Project Structure

The project consists of the following key files and directories:

- `main.py`: The main script to run the application.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `games/`: Directory containing game-related data and modules.
- `assets/`: Contains any static assets used by the application.
- `leaderboard.json`: JSON file that stores the leaderboard data.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**:

   - Click the "Fork" button at the top right of this page.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/your-username/Game-Management-System.git
   cd Game-Management-System
   ```

3. **Create a New Branch**:

   ```bash
   git checkout -b feature-name
   ```

4. **Make Your Changes**:

   - Implement your feature or bug fix.
   - Ensure the code follows the project's coding standards.

5. **Commit and Push**:

   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature-name
   ```

6. **Submit a Pull Request**:

   - Navigate to your forked repository on GitHub.
   - Click the "New Pull Request" button.
   - Provide a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please open an issue on this repository.
