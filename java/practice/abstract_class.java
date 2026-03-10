abstract class shape{
    final double pi = 3.14;
    static int count = 0;
    abstract double CalulateArea();

    shape(){
        count++;
    }

    void displayShape(String name,double area){
        System.out.println("Shape: " + name);
        System.out.println("Area: " + area);
        System.out.println();

    }
}
class circle extends shape{
    double radius;
    circle(double radius){
        this.radius = radius;
    }

    double CalulateArea(){
        return super.pi*radius*radius;
    }
}
class rectangle extends shape{

    double b,l;
    rectangle(double l,double b){
        this.l = l;
        this.b = b;
    }
    double CalulateArea(){
        return l*b;
    }
}
public class practice {
    public static void main(String [] args){
        circle c = new circle(4);
        rectangle r = new rectangle(10,12);
        double c1= c.CalulateArea(),r1=r.CalulateArea();

        c.displayShape("circle",c1);r.displayShape("rectangle",r1);

    }

}
