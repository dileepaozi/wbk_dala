var app = angular.module('bsPubMedicalFacilitiesApp', []);

app.controller("BsPubMedicalFacilitiesController", ['$scope', '$http', function($scope, $http) {


    $scope.district;
    $scope.baselineDate;
    $scope.is_edit = false;
    $scope.submitted = false;

    var init_data = {
        'Table_2': {
            'BmfPubMf': [{
                type_pub_mf: 'Teaching Hospital (TH)',
                number: null,
                male: null,
                female: null,
            }, {
                type_pub_mf: 'Provincial General Hospital (PGH)',
                number: null,
                male: null,
                female: null,
            }, {
                type_pub_mf: 'District General Hospital (DGH)',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Base Hospital (BH )',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Divisional Hospital (DH )',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Rural Hospital (RH )',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Central Dispensary (CH )',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Primary Medical Care Units (PMCU)',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Primary Health Care Centers (PHCC)',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Maternal and Child Health Clinics (MCHC)',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'MOH Offices ',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'Others (Specify)',
                number: null,
                male: null,
                female: null,
            },{
                type_pub_mf: 'TOTAL',
                number: null,
                male: null,
                female: null,
            }],
            'BmfPvtMf': [{
                type_pvt_mf: 'Private Clinics',
                number: null,
                male: null,
                female: null,
            },{
                type_pvt_mf: 'Others',
                number: null,
                male: null,
                female: null,
            },{
                type_pvt_mf: 'TOTAL',
                number: null,
                male: null,
                female: null,
            }]

        }
    }

    $scope.bsDataMedicalFacilities = init_data;


    $scope.saveBsData = function(form) {

    $scope.submitted = true;
       if(form.$valid){

        $http({
            method: 'POST',
            url: '/base_line/bs_save_data',
            contentType: 'application/json; charset=utf-8',
            data: angular.toJson({
                'table_data': $scope.bsDataMedicalFacilities,
                'com_data': {
                    'district': $scope.district,
                    'bs_date':$scope.baselineDate},
                'is_edit': $scope.is_edit
            }),
            dataType: 'json',
        }).then(function successCallback(response) {

            console.log(response);
            $scope.is_edit = false;
            $scope.bsDataMedicalFacilities = init_data;

        }, function errorCallback(response) {

            console.log(response);
        });
        }

    }


    $scope.bsHsDataEdit = function(form)
{
   $scope.submitted = true;
   $scope.is_edit = true;
 if(form.$valid){

    $http({
    method: "POST",
    url: "/base_line/bs_fetch_edit_data",
    data: angular.toJson({
    'table_name': 'Table_2',
    'com_data': {
           'district': $scope.district,
          'bs_date': $scope.baselineDate,
          } }),
    }).success(function(data) {

    console.log(data);
    $scope.bsDataMedicalFacilities = data;
    })

    }


}


    $scope.cancelEdit = function()
{
     $scope.is_edit = false;
     $scope.bsDataMedicalFacilities = init_data;
}



}])
