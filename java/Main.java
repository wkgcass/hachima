import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        String encoded = Hachima.encode("hello, world! 你好，世界！".getBytes(StandardCharsets.UTF_8));
        System.out.println(encoded);
        byte[] decoded = Hachima.decode(encoded);
        System.out.println(new String(decoded));
    }
}
