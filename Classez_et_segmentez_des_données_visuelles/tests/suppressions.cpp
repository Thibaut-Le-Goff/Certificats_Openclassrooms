#include <opencv2/opencv.hpp>

void suppression_bruit(const cv::Mat& image_a_traite, const int& taille_matrice) {

    cv::Mat debruitage_gauzien;
    cv::GaussianBlur(image_a_traite, debruitage_gauzien, cv::Size(taille_matrice, taille_matrice), 0, 0);
    cv::imshow("debruitage_gauzien", debruitage_gauzien);

    cv::Mat debruitage_medien;
    cv::medianBlur(image_a_traite, debruitage_medien, taille_matrice);
    cv::imshow("debruitage_medien", debruitage_medien);

    cv::Mat debruitage_moyen;
    cv::blur(image_a_traite, debruitage_moyen, cv::Size(taille_matrice, taille_matrice));
    cv::imshow("debruitage_moyen", debruitage_moyen);

}