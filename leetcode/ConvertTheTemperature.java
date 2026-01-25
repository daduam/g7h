package leetcode;

class ConvertTheTemperature {

    public double[] convertTemperature(double celsius) {
        return new double[] { toKelvin(celsius), toFahrenheit(celsius) };
    }

    private static double toKelvin(double celsius) {
        return celsius + 273.15;
    }

    private static double toFahrenheit(double celsius) {
        return celsius * 1.80 + 32.00;
    }
}
