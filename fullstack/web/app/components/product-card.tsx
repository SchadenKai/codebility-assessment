import Image from "next/image";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Product } from "@/app/types";

type ProductCardProps = {
  product: Product;
};

export default function ProductCard({ product }: ProductCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{product.product_name}</CardTitle>
        <CardDescription>{product.details}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="relative aspect-square">
          <Image
            src={product.image_url || "/placeholder.svg"}
            alt={product.product_name}
            fill
            className="object-cover"
            loading="lazy"
          />
        </div>
      </CardContent>
      <CardFooter>
        <p>Price: ${product.price}</p>
      </CardFooter>
    </Card>
  );
}
