using namespace std; 


struct  
{
	CurvatureData curvature;
	RgbAData coloring;	
};

struct CurvatureData {
	float maxCurvature;
	float minCurvature;
	float averageSlope;
	float averageDerivativeOfSlope;
};

struct RgbAData {
	uchar r;
	uchar g;
	uchar b;
	uchar alpha;
};

