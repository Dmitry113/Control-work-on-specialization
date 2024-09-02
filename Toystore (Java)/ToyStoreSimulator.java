import java.io.FileWriter;
import java.io.IOException;

public class ToyStoreSimulator {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();

        // Добавляем игрушки
        store.addToy(new ToyItem(1, "конструктор", 2));
        store.addToy(new ToyItem(2, "робот", 2));
        store.addToy(new ToyItem(3, "кукла", 6));

        // Симулируем розыгрыш и записываем результаты в файл
        simulateDraws(store, 10, "draw_results.txt");
    }

    public static void simulateDraws(ToyStore store, int numberOfDraws, String fileName) {
        try (FileWriter writer = new FileWriter(fileName)) {
            for (int i = 0; i < numberOfDraws; i++) {
                int toyId = store.getToyId();
                writer.write(toyId + "\n");
            }
            System.out.println("Результаты успешно записаны в файл " + fileName);
        } catch (IOException e) {
        
        }
    }
}
