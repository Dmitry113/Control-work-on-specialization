public class ToyItem implements Comparable<ToyItem> {
    private final int id;
    private final String name;
    private final int frequency;

    public ToyItem(int id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }

    @Override
    public int compareTo(ToyItem other) {
        return Integer.compare(other.frequency, this.frequency);
    }
}
