#include <opencv2/opencv.hpp>
#include <iostream>

#include "tests/ajouts.h"
#include "tests/suppressions.h"
#include "tests/modifications.h"


int main() {
    cv::Mat image = cv::imread("images/cat.png", cv::IMREAD_GRAYSCALE);

    if (image.empty()) {
        std::cerr << "L'image n'�xiste pas." << std::endl;
        return 1;
    }

    std::cout << "Taille de l'image : " << image.size() << std::endl;

    cv::Mat image_histogramme_etalee;
    cv::equalizeHist(image, image_histogramme_etalee);

    cv::imshow("Image d'origine", image);
    cv::imshow("Image apr�s l'�talement de l'histogramme ", image_histogramme_etalee);

    // rotation de l'image :
    double angle_de_rotation = 45.0;
    cv::Point2f point_de_rotation(image.cols / 2.0, image.rows / 2.0);
    float mise_a_echelle = 0.8;

    cv::Mat image_tournee = rotation(image_histogramme_etalee, point_de_rotation, angle_de_rotation, mise_a_echelle);


    // ajout de bruit
    double moyenne_des_bruits = 0.0;
    double intensite_du_bruit = 50.0;

    cv::Mat image_bruitee = ajout_bruit(image_tournee, moyenne_des_bruits, intensite_du_bruit);


    // tentative de d�bruitage en floutent l'image
    int taille_matrice = 3; 

    suppression_bruit(image_bruitee, taille_matrice);

    cv::waitKey(0);

    return 0;
}