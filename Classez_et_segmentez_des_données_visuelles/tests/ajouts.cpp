#include <opencv2/opencv.hpp>
#include <opencv2/core/mat.hpp>
#include <opencv2/core.hpp>

cv::Mat ajout_bruit(const cv::Mat& image_a_traite, const cv::Scalar& moyenne_des_bruits, const cv::Scalar& intensite_du_bruit) {

    cv::Mat bruit(image_a_traite.size(), CV_8UC1);
    cv::randn(bruit, moyenne_des_bruits, intensite_du_bruit);

    cv::Mat image_bruitee;
    cv::add(image_a_traite, bruit, image_bruitee);
    cv::imshow("Image bruit�e", image_bruitee);

    return image_bruitee;
}