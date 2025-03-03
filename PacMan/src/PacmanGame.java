import javax.sound.sampled.*;
import java.io.*;
import java.io.IOException;
import javax.swing.*;
import javax.swing.Timer;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.util.List;
import java.util.Random;

public class PacmanGame extends JPanel implements ActionListener, KeyListener {
    private final int TILE_SIZE = 50;
    private final int ROWS = 15, COLS = 20;
    private final int END = 15, START = 10;
    private final int POWER_NUM = 40;
    private Point ghostTarget = null;
    private final Image ghostImageBlue = new ImageIcon("src/assert/blue-ghost.png").getImage();
    private final Image ghostImageRed = new ImageIcon("src/assert/red-ghost.png").getImage();
    private final Image ghostImageYellow = new ImageIcon("src/assert/yellow-ghost.png").getImage();
    private final Image pacmanImageRight = new ImageIcon("src/assert/pacman.png").getImage();
    private final Image pacmanImageUp = new ImageIcon("src/assert/pacmanUP.png").getImage();
    private final Image pacmanImageDown = new ImageIcon("src/assert/pacmanDown.png").getImage();
    private final Image pacmanImageLeft = new ImageIcon("src/assert/pacmanLeft.png").getImage();
    private Image pacmanImage = pacmanImageRight;

    private final int[][] maze1 = {
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
            {1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1},
            {1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1},
            {1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1},
            {1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1},
            {1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1},
            {1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1},
            {1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1},
            {1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1},
            {1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1},
            {1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1},
            {1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1},
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
    };
    private final int[][] maze2 = {
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
            {1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1},
            {1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1},
            {1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1},
            {1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1},
            {1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1},
            {1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1},
            {1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1},
            {1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1},
            {1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1},
            {1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1},
            {1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1},
            {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}

    };
    private final int[][] maze3 = {
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
            {1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1},
            {1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1},
            {1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1},
            {1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1},
            {1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1},
            {1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1},
            {1,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1},
            {1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1},
            {1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1},
            {1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1},
            {1,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1},
            {1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1},
            {1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1},
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
    };
    private final int [][][] levels = {maze1,maze2,maze3};
    private int level = 0;

    private Point pacman = new Point(1, 1);
    private List<Point> ghosts = new ArrayList<>(Arrays.asList(new Point(18, 13), new Point(15, 7), new Point(10, 5)));
    private boolean[][] dots = new boolean[ROWS][COLS];
    private Timer timer;
    private int points = 0;
    private int score = 0;
    private boolean ghostsFleeing = false;
    private Random random = new Random();
    private int counter = random.nextInt((END - START) + 1) + START;
    private Clip clip, clipChomp, clipGhost;
    private String fileName = "data.txt";
    private Map<Integer,String> leaderboard = new HashMap<>();
    private int[][] maze;
    private JLabel scoreLabel;

    public PacmanGame() {
        maze = levels[0];
        readFromFile();
        setPreferredSize(new Dimension(COLS * TILE_SIZE, ROWS * TILE_SIZE));
        setBackground(Color.BLACK);
        addKeyListener(this);
        setFocusable(true);
        generateDots();
        scoreLabel = new JLabel("    Score: 0                      Point: 0");
        scoreLabel.setFont(new Font("Arial", Font.BOLD, 20));
        this.add(scoreLabel, BorderLayout.NORTH);
        this.setVisible(true);

        timer = new Timer(400, this);
        timer.start();

        playBackgroundMusic();

    }

    private void readFromFile(){
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            String[] words;
            while ((line = reader.readLine()) != null) {
                words = line.split(":");
                leaderboard.put(Integer.parseInt(words[0]),words[1]);
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    private void writeToFile(){
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for(Integer score : leaderboard.keySet()){
                writer.write(score + ":" + leaderboard.get(score) + "\n");
            }

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    private void manegeLeaderBoard(int score,String name){
        int min = score;
        if(leaderboard.size() < 3) {
            leaderboard.put(score, name);
        }
        else{
            for (Integer oldScore : leaderboard.keySet()) {
                if (score == oldScore) {
                    leaderboard.replace(oldScore, name + "," + leaderboard.get(oldScore));
                    return;
                } else if (min > oldScore) {
                    min = oldScore;
                }
            }
            if (min != score) {
                leaderboard.remove(min);
                leaderboard.put(score, name);
            }
        }
    }

    private void playBackgroundMusic() {
        try {
            File musicFile = new File("src/assert/backgroundMusic.wav");
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(musicFile);
            clip = AudioSystem.getClip();
            clip.open(audioStream);
            FloatControl gainControl = (FloatControl) clip.getControl(FloatControl.Type.MASTER_GAIN);
            gainControl.setValue(-10.0f);
            clip.loop(Clip.LOOP_CONTINUOUSLY);// מוסיקה ברקע שמנגנת שוב ושוב
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }

    private void playChompMusic(){
        try{
            File musicFile = new File("src/assert/completetask.wav");
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(musicFile);
            clipChomp = AudioSystem.getClip();
            clipChomp.open(audioStream);
            FloatControl gainControl = (FloatControl) clipChomp.getControl(FloatControl.Type.MASTER_GAIN);
            gainControl.setValue(-10.0f);
            clipChomp.start();
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }

    private void playGhostMusic(){
        try{
            File musicFile = new File("src/assert/ghost.wav");
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(musicFile);
            clipGhost = AudioSystem.getClip();
            clipGhost.open(audioStream);
            clip.stop();
            if(clipChomp!=null) {
                clipChomp.stop();
            }
            clipGhost.start();
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }

    private List<Point> bfsPath(Point start, Point target) {
        Queue<Point> queue = new LinkedList<>();
        Map<Point, Point> cameFrom = new HashMap<>();
        queue.add(start);
        cameFrom.put(start, null);

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            if (current.equals(target)) break;
            for (Point dir : new Point[]{new Point(1,0), new Point(-1,0), new Point(0,1), new Point(0,-1)}) {
                Point next = new Point(current.x + dir.x, current.y + dir.y);
                if (next.x >= 0 && next.x < COLS && next.y >= 0 && next.y < ROWS && maze[next.y][next.x] == 0 && !cameFrom.containsKey(next)) {
                    queue.add(next);
                    cameFrom.put(next, current);
                }
            }
        }

        List<Point> path = new ArrayList<>();
        Point step = target;
        while (cameFrom.containsKey(step) && cameFrom.get(step) != null) {
            path.add(step);
            step = cameFrom.get(step);
        }
        Collections.reverse(path);
        return path;
    }

    private void generateDots() {
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (maze[r][c] == 0)
                    dots[r][c] = true;
                else{
                    dots[r][c] = false;
                }
            }
        }
        dots[pacman.y][pacman.x] = false;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Point target;
        for (int i = 0; i < ghosts.size(); i++) {
            target = pacman;
            if(ghostTarget != null && ghosts.get(i).getLocation() != ghostTarget){
                target = ghostTarget;
            }
            else if(ghosts.get(i).getLocation() == ghostTarget){
                ghostTarget = null;
                ghostsFleeing = false;
            }
            List<Point> path = bfsPath(ghosts.get(i), target);
            if (!path.isEmpty()) ghosts.set(i, path.get(0));
            else{
                ghostTarget = null;
                ghostsFleeing = false;
            }
        }
        checkGameOver();
        repaint();
    }

    private void checkGameOver() {
        for (Point ghost : ghosts) {
            if (ghost.equals(pacman) && !ghostsFleeing) {
                playGhostMusic();
                showGameOver("Game Over! You were caught!\nYour Score Is: " + score,true);
                score = 0;
                scoreLabel.setText("    Score: " + score + "                      Point: " + points);
                return;
            }
        }

        boolean allDotsCollected = true;
        for (boolean[] row : dots) {
            for (boolean dot : row) {
                if (dot) {
                    allDotsCollected = false;
                    break;
                }
            }
        }

        if (allDotsCollected) {
            showGameOver("Congratulations! You collected all the dots!\nYour Score Is: " + score,false);
        }
    }

    private void showGameOver(String message,boolean isEnd) {
        timer.stop();
        int option;
        String mes, title;
        if(isEnd) {
            mes = "\nPlay Again?";
            title = "GAME OVER";
        }
        else{
            mes = "\nmove to next level?";
            title = "GREAT GAME";
        }
        option = JOptionPane.showConfirmDialog(this, message + mes, title, JOptionPane.YES_NO_OPTION);
        if (option == JOptionPane.YES_OPTION) {
            level++;
            if(level==3||isEnd){
                level=0;
            }
            maze = levels[level];
            if(isEnd){
                String playerName = JOptionPane.showInputDialog(this, "Enter your name:", "Save Score", JOptionPane.PLAIN_MESSAGE);

                if (playerName != null && !playerName.trim().isEmpty()) {
                    System.out.println("Player name: " + playerName);
                    manegeLeaderBoard(score,playerName);
                }
                JOptionPane.showMessageDialog(this, getStringOfLeaderboard(), "leaderboard", JOptionPane.INFORMATION_MESSAGE);
            }
            resetGame();
        } else {
            String playerName = JOptionPane.showInputDialog(this, "Enter your name:", "Save Score", JOptionPane.PLAIN_MESSAGE);

            if (playerName != null && !playerName.trim().isEmpty()) {
                System.out.println("Player name: " + playerName);
                manegeLeaderBoard(score,playerName);
            }
            JOptionPane.showMessageDialog(this, getStringOfLeaderboard(), "leaderboard", JOptionPane.INFORMATION_MESSAGE);

            writeToFile();
            System.exit(0);
        }
    }

    private String getStringOfLeaderboard(){
        List<Integer> keys = new ArrayList<>(leaderboard.keySet());

        keys.sort(Collections.reverseOrder());

        StringBuilder result = new StringBuilder();
        for (int key : keys) {
            result.append(key).append(" = ").append(leaderboard.get(key)).append("\n");
        }

        return result.toString();
    }

    private void resetGame() {
        pacman = new Point(1, 1);
        ghosts = new ArrayList<>(Arrays.asList(new Point(18, 13), new Point(15, 7), new Point(10, 5)));
        points = 0;
        generateDots();
        clip.start();
        pacmanImage = pacmanImageRight;
        scoreLabel.setText("    Score: " + score + "                      Point: " + points);
        timer.start();
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (maze[r][c] == 1) {
                    if((r==7 && (c==0 || c==19)) || (c==10 && (r==0 || r==14))){
                        g.setColor(Color.orange);
                        g.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
                    }
                    else{
                        g.setColor(Color.BLUE);
                        g.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE);
                    }
                } else if (dots[r][c]) {
                    g.setColor(Color.WHITE);
                    g.fillOval(c * TILE_SIZE + TILE_SIZE / 3, r * TILE_SIZE + TILE_SIZE / 3, TILE_SIZE / 3, TILE_SIZE / 3);
                }
            }
        }
        if(points >= POWER_NUM){
            g.drawImage(pacmanImage, pacman.x * TILE_SIZE, pacman.y * TILE_SIZE, TILE_SIZE, TILE_SIZE,this);
        }
        else{
            g.drawImage(pacmanImage, pacman.x * TILE_SIZE+5, pacman.y * TILE_SIZE+5, TILE_SIZE-10, TILE_SIZE-10,this);
        }

        Point ghost;
        if(ghostsFleeing) {
            counter++;
            if (counter % 2 == 0){
                for (int i = 0; i < ghosts.size(); i++) {
                    ghost = ghosts.get(i);
                    if (i == 0) {
                        g.drawImage(ghostImageBlue, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                    } else if (i == 1) {
                        g.drawImage(ghostImageRed, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                    } else {
                        g.drawImage(ghostImageYellow, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                    }
                }
            }
        }
        else {
            for (int i = 0; i < ghosts.size(); i++) {
                ghost = ghosts.get(i);
                if (i == 0) {
                    g.drawImage(ghostImageBlue, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                } else if (i == 1) {
                    g.drawImage(ghostImageRed, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                } else {
                    g.drawImage(ghostImageYellow, ghost.x * TILE_SIZE, ghost.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, this);
                }
            }
        }
    }

    private void countAndChangeDots(int x, int y){
        if(dots[y][x]){
            dots[y][x] = false;
            playChompMusic();
            points += 1;
            score += 1;
            scoreLabel.setText("    Score: " + score + "                      Point: " + points);
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int dx = 0, dy = 0;
        switch (e.getKeyCode()) {
            case KeyEvent.VK_UP: dy = -1;pacmanImage = pacmanImageUp; break;
            case KeyEvent.VK_DOWN: dy = 1;pacmanImage = pacmanImageDown; break;
            case KeyEvent.VK_LEFT: dx = -1;pacmanImage = pacmanImageLeft; break;
            case KeyEvent.VK_RIGHT: dx = 1;pacmanImage = pacmanImageRight; break;
            case KeyEvent.VK_SPACE:
                if(points >= POWER_NUM){
                    points -= POWER_NUM;
                    ghostTarget = new Point(10,5);
                    ghostsFleeing = true;
                    scoreLabel.setText("    Score: " + score + "                      Point: " + points);

                }
                break;
        }
        Point newPacman = new Point(pacman.x + dx, pacman.y + dy);
        if(maze[newPacman.y][newPacman.x] == 1) {
            if(newPacman.y == 7 && newPacman.x == 0){
                newPacman = new Point(18,7);
                pacman = newPacman;
                countAndChangeDots(pacman.x,pacman.y);
            }
            else if(newPacman.y == 7 && newPacman.x == 19){
                newPacman = new Point(1,7);
                pacman = newPacman;
                countAndChangeDots(pacman.x,pacman.y);
            }
            else if(newPacman.y == 0 && newPacman.x == 10){
                newPacman = new Point(10,13);
                pacman = newPacman;
                countAndChangeDots(pacman.x,pacman.y);
            }
            else if(newPacman.y == 14 && newPacman.x == 10){
                newPacman = new Point(10,1);
                pacman = newPacman;
                countAndChangeDots(pacman.x,pacman.y);
            }

        }
        else{
            pacman = newPacman;
            countAndChangeDots(pacman.x,pacman.y);
        }
        repaint();
    }

    @Override public void keyReleased(KeyEvent e) {}
    @Override public void keyTyped(KeyEvent e) {}

    public static void main(String[] args) {
        JFrame frame = new JFrame("Pac-Man AI");
        PacmanGame game = new PacmanGame();
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
