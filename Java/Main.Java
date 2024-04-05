Class main{
    public static void main (String[] 
    args) {
        System.out.printl
        ("Inicializando...");
        System.out.println("Car...");
        Car car = new Car("AMQ123", new 
        Account ("Andres Loiza", "ADN1235", 
        "andresl@hotmail.com", "12365"));
        car.passenger= 4;
        car.printdataCar();

        System.out.println("Uberx....")
        Uberx uberx = new Uberx
        ("MKL185", new Account ("Maria Loyola", "JKL12365", 
        "marial@hotmail.com", "125478"),
        "Toyota", "corolla");    

}