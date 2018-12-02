package day1;

import java.util.HashSet;
import java.util.Set;

public class day1 {
    public static int star1(String test) {
        String[] lines = test.split("\n");
        int sum = 0;

        for (int i = 0; i < lines.length; i++) {
            sum += Integer.parseInt(lines[i]);
        }

        return sum;
    }

    public static int star2(String test) {
        String[] lines = test.split("\n");
        int currentSum = 0;

        Set<Integer> seen = new HashSet<Integer>();
        seen.add(0);


        while (true) {
            for (String i : lines) {
                currentSum += Integer.parseInt(i);

                if (seen.contains(currentSum)) {
                    return currentSum;
                }

                seen.add(currentSum);
            }
        }
    }
}