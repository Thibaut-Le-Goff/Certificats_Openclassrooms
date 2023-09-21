#include <opencv2/opencv.hpp>

cv::Mat rotation(const cv::Mat& image_a_traite, const cv::Point2f& point_de_rotation, const double& angle_de_rotation, const float& mise_a_echelle) {

    cv::Mat matrice_de_rotation = cv::getRotationMatrix2D(point_de_rotation, angle_de_rotation, mise_a_echelle);
    std::cout << "Matrice de rotaton :" << matrice_de_rotation << std::endl;

    cv::Mat image_tournee;
    cv::warpAffine(image_a_traite, image_tournee, matrice_de_rotation, image_a_traite.size());
    cv::imshow("Image tourn�e", image_tournee);

    return image_tournee;
}