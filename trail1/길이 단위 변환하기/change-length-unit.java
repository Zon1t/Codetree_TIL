public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        double ft_to_cm = 30.48;
        int mi_to_cm = 160934;
        
        double ft = 9.2, mi = 1.3;
        System.out.printf("%.1fft = %.1fcm\n", ft, ft*ft_to_cm);
        System.out.printf("%.1fmi = %.1fcm", mi, mi*mi_to_cm);
    }
}