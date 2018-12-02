import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

import day1.*;

class AoS {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();
        int star = sc.nextInt();

        String input = new String(Files.readAllBytes(Paths.get("./input/day" + Integer.toString(day) + ".txt")));

        switch (Integer.toString(day) + "," + Integer.toString(star)) {
            case "1,1":
                System.out.println(day1.star1(input));
                break;
            case "1,2":
                System.out.println(day1.star2(input));
                break;
        }
    }
}