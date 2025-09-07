import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

class Hachima {
    private static final Map<Character, Character> H2B = new HashMap<Character, Character>();
    private static final Map<Character, Character> B2H = new HashMap<Character, Character>();

    static {
        final String[] HACHIMA = "哈、基、米、南、北、绿、豆、阿、西、噶、压、库、那、鲁、曼、波、欧、马、自、立、悠、嗒、步、诺、斯、哇、嗷、冰、踩、背、叮、咚、鸡、大、狗、叫、袋、鼠、兴、奋、剂、出、示、健、康、码、楼、上、下、来、带、一、段、小、白、手、套、胖、宝、牛、魔、呵、嘿、喔".split("、");
        final char[] BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".toCharArray();
        for (int i = 0; i < HACHIMA.length; ++i) {
            H2B.put(HACHIMA[i].charAt(0), BASE64[i]);
            B2H.put(BASE64[i], HACHIMA[i].charAt(0));
        }
    }

    private Hachima() {
    }

    public static String encode(byte[] bytes) {
        String encoded = Base64.getEncoder().encodeToString(bytes);
        char[] chars = encoded.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            if (c == '=') {
                continue;
            }
            sb.append(B2H.get(c));
        }
        return sb.toString();
    }

    public static byte[] decode(String hachima) {
        char[] chars = hachima.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            sb.append(H2B.get(c));
        }
        int padding = 4 - (sb.length() % 4);
        if (padding != 4) {
            for (int i = 0; i < padding; ++i) {
                sb.append('=');
            }
        }
        String base64str = sb.toString();
        return Base64.getDecoder().decode(base64str);
    }
}
