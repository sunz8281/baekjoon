import java.util.Scanner;

public class A27866 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        System.out.println(str.charAt(n-1));
        sc.close();
    }
}