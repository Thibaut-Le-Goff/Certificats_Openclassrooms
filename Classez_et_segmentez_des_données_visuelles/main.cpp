#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    cv::Mat image = cv::imread("cat.png", cv::IMREAD_GRAYSCALE);

    if (image.empty()) {
        std::cerr << "L'image n'éxiste pas." << std::endl;
        return 1;
    }

    std::cout << "Taille de l'image : " << image.size() << std::endl;

    cv::Mat image_histogramme_etalee;
    cv::equalizeHist(image, image_histogramme_etalee);

    cv::imshow("Image d'origine", image);
    cv::imshow("Image après l'étalement de l'histogramme ", image_histogramme_etalee);

    // rotation de l'image :
    double angle_de_rotation = 45.0;
    cv::Point2f point_de_rotation(image.cols / 2.0, image.rows / 2.0);
    float mise_a_echelle = 0.8;

    cv::Mat matrice_de_rotation = cv::getRotationMatrix2D(point_de_rotation, angle_de_rotation, mise_a_echelle);
    std::cout << "Matrice de rotaton :" << matrice_de_rotation << std::endl;

    cv::Mat image_tournee;
    cv::warpAffine(image_histogramme_etalee, image_tournee, matrice_de_rotation, image_histogramme_etalee.size());
    cv::imshow("Image tournée", image_tournee);

    // ajout de bruit
    double moyenne_des_bruits = 0.0;    
    double intensite_du_bruit = 25.0; 

    cv::Mat bruit(image.size(), CV_8UC1);
    cv::randn(bruit, moyenne_des_bruits, intensite_du_bruit);

    cv::Mat image_bruitee;
    cv::add(image_tournee, bruit, image_bruitee);
    cv::imshow("Image bruitée", image_bruitee);

    cv::waitKey(0);

    return 0;
}