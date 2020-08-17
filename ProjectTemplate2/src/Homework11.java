import components.naturalnumber.NaturalNumber;
import components.naturalnumber.NaturalNumber2;
import components.simplereader.SimpleReader;
import components.simplereader.SimpleReader1L;
import components.simplewriter.SimpleWriter;
import components.simplewriter.SimpleWriter1L;

/**
 * Put a short phrase describing the program here.
 *
 * @author Put your name here
 *
 */
public final class Homework11 {

    /**
     * Private constructor so this utility class cannot be instantiated.
     */
    private Homework11() {
    }

    /**
     * Returns the number of digits of {@code n}.
     *
     * @param n
     *            {@code NaturalNumber} whose digits to count
     * @return the number of digits of {@code n}
     * @ensures numberOfDigits = [number of digits of n]
     */
    private static int numberOfDigits(NaturalNumber n) {
        int length = 0;
        while (!n.isZero()) {
            if (!n.isZero()) {
                n.divideBy10();
                //numberOfDigits(n);
                length++;
            }
        }

        return length;
    }

    /**
     * Main method.
     *
     * @param args
     *            the command line arguments
     */
    public static void main(String[] args) {
        SimpleReader in = new SimpleReader1L();
        SimpleWriter out = new SimpleWriter1L();
        /*
         * Put your main program code here; it may call myMethod as shown
         */
        String test1String = in.nextLine();
        NaturalNumber test1 = new NaturalNumber2(test1String);
        int test1Digits = numberOfDigits(test1);
        out.println(test1Digits);
        /*
         * Close input and output streams
         */
        in.close();
        out.close();
    }

}
