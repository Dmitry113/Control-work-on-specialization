import java.util.PriorityQueue;
import java.util.Random;

public class ToyStore {
    private final PriorityQueue<ToyItem> toyQueue;
    private final Random random;

    public ToyStore() {
        toyQueue = new PriorityQueue<>();
        random = new Random();
    }

    public void addToy(ToyItem toy) {
        toyQueue.add(toy);
    }

    public int getToyId() {
        int randomNumber = random.nextInt(10) + 1; // Получаем случайное число от 1 до 10
        if (randomNumber <= 2) {
            return 1;  // 20% шанс
        } else if (randomNumber <= 4) {
            return 2;  // 20% шанс
        } else {
            return 3;  // 60% шанс
        }
    }
}
