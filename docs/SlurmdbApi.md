# slurmrestapi.SlurmdbApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurmdb_v0041_delete_account**](SlurmdbApi.md#slurmdb_v0041_delete_account) | **DELETE** /slurmdb/v0.0.41/account/{account_name} | Delete account
[**slurmdb_v0041_delete_association**](SlurmdbApi.md#slurmdb_v0041_delete_association) | **DELETE** /slurmdb/v0.0.41/association/ | Delete association
[**slurmdb_v0041_delete_associations**](SlurmdbApi.md#slurmdb_v0041_delete_associations) | **DELETE** /slurmdb/v0.0.41/associations/ | Delete associations
[**slurmdb_v0041_delete_cluster**](SlurmdbApi.md#slurmdb_v0041_delete_cluster) | **DELETE** /slurmdb/v0.0.41/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0041_delete_single_qos**](SlurmdbApi.md#slurmdb_v0041_delete_single_qos) | **DELETE** /slurmdb/v0.0.41/qos/{qos} | Delete QOS
[**slurmdb_v0041_delete_user**](SlurmdbApi.md#slurmdb_v0041_delete_user) | **DELETE** /slurmdb/v0.0.41/user/{name} | Delete user
[**slurmdb_v0041_delete_wckey**](SlurmdbApi.md#slurmdb_v0041_delete_wckey) | **DELETE** /slurmdb/v0.0.41/wckey/{id} | Delete wckey
[**slurmdb_v0041_get_account**](SlurmdbApi.md#slurmdb_v0041_get_account) | **GET** /slurmdb/v0.0.41/account/{account_name} | Get account info
[**slurmdb_v0041_get_accounts**](SlurmdbApi.md#slurmdb_v0041_get_accounts) | **GET** /slurmdb/v0.0.41/accounts/ | Get account list
[**slurmdb_v0041_get_association**](SlurmdbApi.md#slurmdb_v0041_get_association) | **GET** /slurmdb/v0.0.41/association/ | Get association info
[**slurmdb_v0041_get_associations**](SlurmdbApi.md#slurmdb_v0041_get_associations) | **GET** /slurmdb/v0.0.41/associations/ | Get association list
[**slurmdb_v0041_get_cluster**](SlurmdbApi.md#slurmdb_v0041_get_cluster) | **GET** /slurmdb/v0.0.41/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0041_get_clusters**](SlurmdbApi.md#slurmdb_v0041_get_clusters) | **GET** /slurmdb/v0.0.41/clusters/ | Get cluster list
[**slurmdb_v0041_get_config**](SlurmdbApi.md#slurmdb_v0041_get_config) | **GET** /slurmdb/v0.0.41/config | Dump all configuration information
[**slurmdb_v0041_get_diag**](SlurmdbApi.md#slurmdb_v0041_get_diag) | **GET** /slurmdb/v0.0.41/diag/ | Get slurmdb diagnostics
[**slurmdb_v0041_get_instance**](SlurmdbApi.md#slurmdb_v0041_get_instance) | **GET** /slurmdb/v0.0.41/instance/ | Get instance info
[**slurmdb_v0041_get_instances**](SlurmdbApi.md#slurmdb_v0041_get_instances) | **GET** /slurmdb/v0.0.41/instances/ | Get instance list
[**slurmdb_v0041_get_job**](SlurmdbApi.md#slurmdb_v0041_get_job) | **GET** /slurmdb/v0.0.41/job/{job_id} | Get job info
[**slurmdb_v0041_get_jobs**](SlurmdbApi.md#slurmdb_v0041_get_jobs) | **GET** /slurmdb/v0.0.41/jobs/ | Get job list
[**slurmdb_v0041_get_qos**](SlurmdbApi.md#slurmdb_v0041_get_qos) | **GET** /slurmdb/v0.0.41/qos/ | Get QOS list
[**slurmdb_v0041_get_single_qos**](SlurmdbApi.md#slurmdb_v0041_get_single_qos) | **GET** /slurmdb/v0.0.41/qos/{qos} | Get QOS info
[**slurmdb_v0041_get_tres**](SlurmdbApi.md#slurmdb_v0041_get_tres) | **GET** /slurmdb/v0.0.41/tres/ | Get TRES info
[**slurmdb_v0041_get_user**](SlurmdbApi.md#slurmdb_v0041_get_user) | **GET** /slurmdb/v0.0.41/user/{name} | Get user info
[**slurmdb_v0041_get_users**](SlurmdbApi.md#slurmdb_v0041_get_users) | **GET** /slurmdb/v0.0.41/users/ | Get user list
[**slurmdb_v0041_get_wckey**](SlurmdbApi.md#slurmdb_v0041_get_wckey) | **GET** /slurmdb/v0.0.41/wckey/{id} | Get wckey info
[**slurmdb_v0041_get_wckeys**](SlurmdbApi.md#slurmdb_v0041_get_wckeys) | **GET** /slurmdb/v0.0.41/wckeys/ | Get wckey list
[**slurmdb_v0041_post_accounts**](SlurmdbApi.md#slurmdb_v0041_post_accounts) | **POST** /slurmdb/v0.0.41/accounts/ | Add/update list of accounts
[**slurmdb_v0041_post_accounts_association**](SlurmdbApi.md#slurmdb_v0041_post_accounts_association) | **POST** /slurmdb/v0.0.41/accounts_association/ | Add accounts with conditional association
[**slurmdb_v0041_post_associations**](SlurmdbApi.md#slurmdb_v0041_post_associations) | **POST** /slurmdb/v0.0.41/associations/ | Set associations info
[**slurmdb_v0041_post_clusters**](SlurmdbApi.md#slurmdb_v0041_post_clusters) | **POST** /slurmdb/v0.0.41/clusters/ | Get cluster list
[**slurmdb_v0041_post_config**](SlurmdbApi.md#slurmdb_v0041_post_config) | **POST** /slurmdb/v0.0.41/config | Load all configuration information
[**slurmdb_v0041_post_qos**](SlurmdbApi.md#slurmdb_v0041_post_qos) | **POST** /slurmdb/v0.0.41/qos/ | Add or update QOSs
[**slurmdb_v0041_post_tres**](SlurmdbApi.md#slurmdb_v0041_post_tres) | **POST** /slurmdb/v0.0.41/tres/ | Add TRES
[**slurmdb_v0041_post_users**](SlurmdbApi.md#slurmdb_v0041_post_users) | **POST** /slurmdb/v0.0.41/users/ | Update users
[**slurmdb_v0041_post_users_association**](SlurmdbApi.md#slurmdb_v0041_post_users_association) | **POST** /slurmdb/v0.0.41/users_association/ | Add users with conditional association
[**slurmdb_v0041_post_wckeys**](SlurmdbApi.md#slurmdb_v0041_post_wckeys) | **POST** /slurmdb/v0.0.41/wckeys/ | Add or update wckeys
[**slurmdb_v0042_delete_account**](SlurmdbApi.md#slurmdb_v0042_delete_account) | **DELETE** /slurmdb/v0.0.42/account/{account_name} | Delete account
[**slurmdb_v0042_delete_association**](SlurmdbApi.md#slurmdb_v0042_delete_association) | **DELETE** /slurmdb/v0.0.42/association/ | Delete association
[**slurmdb_v0042_delete_associations**](SlurmdbApi.md#slurmdb_v0042_delete_associations) | **DELETE** /slurmdb/v0.0.42/associations/ | Delete associations
[**slurmdb_v0042_delete_cluster**](SlurmdbApi.md#slurmdb_v0042_delete_cluster) | **DELETE** /slurmdb/v0.0.42/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0042_delete_single_qos**](SlurmdbApi.md#slurmdb_v0042_delete_single_qos) | **DELETE** /slurmdb/v0.0.42/qos/{qos} | Delete QOS
[**slurmdb_v0042_delete_user**](SlurmdbApi.md#slurmdb_v0042_delete_user) | **DELETE** /slurmdb/v0.0.42/user/{name} | Delete user
[**slurmdb_v0042_delete_wckey**](SlurmdbApi.md#slurmdb_v0042_delete_wckey) | **DELETE** /slurmdb/v0.0.42/wckey/{id} | Delete wckey
[**slurmdb_v0042_get_account**](SlurmdbApi.md#slurmdb_v0042_get_account) | **GET** /slurmdb/v0.0.42/account/{account_name} | Get account info
[**slurmdb_v0042_get_accounts**](SlurmdbApi.md#slurmdb_v0042_get_accounts) | **GET** /slurmdb/v0.0.42/accounts/ | Get account list
[**slurmdb_v0042_get_association**](SlurmdbApi.md#slurmdb_v0042_get_association) | **GET** /slurmdb/v0.0.42/association/ | Get association info
[**slurmdb_v0042_get_associations**](SlurmdbApi.md#slurmdb_v0042_get_associations) | **GET** /slurmdb/v0.0.42/associations/ | Get association list
[**slurmdb_v0042_get_cluster**](SlurmdbApi.md#slurmdb_v0042_get_cluster) | **GET** /slurmdb/v0.0.42/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0042_get_clusters**](SlurmdbApi.md#slurmdb_v0042_get_clusters) | **GET** /slurmdb/v0.0.42/clusters/ | Get cluster list
[**slurmdb_v0042_get_config**](SlurmdbApi.md#slurmdb_v0042_get_config) | **GET** /slurmdb/v0.0.42/config | Dump all configuration information
[**slurmdb_v0042_get_diag**](SlurmdbApi.md#slurmdb_v0042_get_diag) | **GET** /slurmdb/v0.0.42/diag/ | Get slurmdb diagnostics
[**slurmdb_v0042_get_instance**](SlurmdbApi.md#slurmdb_v0042_get_instance) | **GET** /slurmdb/v0.0.42/instance/ | Get instance info
[**slurmdb_v0042_get_instances**](SlurmdbApi.md#slurmdb_v0042_get_instances) | **GET** /slurmdb/v0.0.42/instances/ | Get instance list
[**slurmdb_v0042_get_job**](SlurmdbApi.md#slurmdb_v0042_get_job) | **GET** /slurmdb/v0.0.42/job/{job_id} | Get job info
[**slurmdb_v0042_get_jobs**](SlurmdbApi.md#slurmdb_v0042_get_jobs) | **GET** /slurmdb/v0.0.42/jobs/ | Get job list
[**slurmdb_v0042_get_ping**](SlurmdbApi.md#slurmdb_v0042_get_ping) | **GET** /slurmdb/v0.0.42/ping/ | ping test
[**slurmdb_v0042_get_qos**](SlurmdbApi.md#slurmdb_v0042_get_qos) | **GET** /slurmdb/v0.0.42/qos/ | Get QOS list
[**slurmdb_v0042_get_single_qos**](SlurmdbApi.md#slurmdb_v0042_get_single_qos) | **GET** /slurmdb/v0.0.42/qos/{qos} | Get QOS info
[**slurmdb_v0042_get_tres**](SlurmdbApi.md#slurmdb_v0042_get_tres) | **GET** /slurmdb/v0.0.42/tres/ | Get TRES info
[**slurmdb_v0042_get_user**](SlurmdbApi.md#slurmdb_v0042_get_user) | **GET** /slurmdb/v0.0.42/user/{name} | Get user info
[**slurmdb_v0042_get_users**](SlurmdbApi.md#slurmdb_v0042_get_users) | **GET** /slurmdb/v0.0.42/users/ | Get user list
[**slurmdb_v0042_get_wckey**](SlurmdbApi.md#slurmdb_v0042_get_wckey) | **GET** /slurmdb/v0.0.42/wckey/{id} | Get wckey info
[**slurmdb_v0042_get_wckeys**](SlurmdbApi.md#slurmdb_v0042_get_wckeys) | **GET** /slurmdb/v0.0.42/wckeys/ | Get wckey list
[**slurmdb_v0042_post_accounts**](SlurmdbApi.md#slurmdb_v0042_post_accounts) | **POST** /slurmdb/v0.0.42/accounts/ | Add/update list of accounts
[**slurmdb_v0042_post_accounts_association**](SlurmdbApi.md#slurmdb_v0042_post_accounts_association) | **POST** /slurmdb/v0.0.42/accounts_association/ | Add accounts with conditional association
[**slurmdb_v0042_post_associations**](SlurmdbApi.md#slurmdb_v0042_post_associations) | **POST** /slurmdb/v0.0.42/associations/ | Set associations info
[**slurmdb_v0042_post_clusters**](SlurmdbApi.md#slurmdb_v0042_post_clusters) | **POST** /slurmdb/v0.0.42/clusters/ | Get cluster list
[**slurmdb_v0042_post_config**](SlurmdbApi.md#slurmdb_v0042_post_config) | **POST** /slurmdb/v0.0.42/config | Load all configuration information
[**slurmdb_v0042_post_qos**](SlurmdbApi.md#slurmdb_v0042_post_qos) | **POST** /slurmdb/v0.0.42/qos/ | Add or update QOSs
[**slurmdb_v0042_post_tres**](SlurmdbApi.md#slurmdb_v0042_post_tres) | **POST** /slurmdb/v0.0.42/tres/ | Add TRES
[**slurmdb_v0042_post_users**](SlurmdbApi.md#slurmdb_v0042_post_users) | **POST** /slurmdb/v0.0.42/users/ | Update users
[**slurmdb_v0042_post_users_association**](SlurmdbApi.md#slurmdb_v0042_post_users_association) | **POST** /slurmdb/v0.0.42/users_association/ | Add users with conditional association
[**slurmdb_v0042_post_wckeys**](SlurmdbApi.md#slurmdb_v0042_post_wckeys) | **POST** /slurmdb/v0.0.42/wckeys/ | Add or update wckeys
[**slurmdb_v0043_delete_account**](SlurmdbApi.md#slurmdb_v0043_delete_account) | **DELETE** /slurmdb/v0.0.43/account/{account_name} | Delete account
[**slurmdb_v0043_delete_association**](SlurmdbApi.md#slurmdb_v0043_delete_association) | **DELETE** /slurmdb/v0.0.43/association/ | Delete association
[**slurmdb_v0043_delete_associations**](SlurmdbApi.md#slurmdb_v0043_delete_associations) | **DELETE** /slurmdb/v0.0.43/associations/ | Delete associations
[**slurmdb_v0043_delete_cluster**](SlurmdbApi.md#slurmdb_v0043_delete_cluster) | **DELETE** /slurmdb/v0.0.43/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0043_delete_single_qos**](SlurmdbApi.md#slurmdb_v0043_delete_single_qos) | **DELETE** /slurmdb/v0.0.43/qos/{qos} | Delete QOS
[**slurmdb_v0043_delete_user**](SlurmdbApi.md#slurmdb_v0043_delete_user) | **DELETE** /slurmdb/v0.0.43/user/{name} | Delete user
[**slurmdb_v0043_delete_wckey**](SlurmdbApi.md#slurmdb_v0043_delete_wckey) | **DELETE** /slurmdb/v0.0.43/wckey/{id} | Delete wckey
[**slurmdb_v0043_get_account**](SlurmdbApi.md#slurmdb_v0043_get_account) | **GET** /slurmdb/v0.0.43/account/{account_name} | Get account info
[**slurmdb_v0043_get_accounts**](SlurmdbApi.md#slurmdb_v0043_get_accounts) | **GET** /slurmdb/v0.0.43/accounts/ | Get account list
[**slurmdb_v0043_get_association**](SlurmdbApi.md#slurmdb_v0043_get_association) | **GET** /slurmdb/v0.0.43/association/ | Get association info
[**slurmdb_v0043_get_associations**](SlurmdbApi.md#slurmdb_v0043_get_associations) | **GET** /slurmdb/v0.0.43/associations/ | Get association list
[**slurmdb_v0043_get_cluster**](SlurmdbApi.md#slurmdb_v0043_get_cluster) | **GET** /slurmdb/v0.0.43/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0043_get_clusters**](SlurmdbApi.md#slurmdb_v0043_get_clusters) | **GET** /slurmdb/v0.0.43/clusters/ | Get cluster list
[**slurmdb_v0043_get_config**](SlurmdbApi.md#slurmdb_v0043_get_config) | **GET** /slurmdb/v0.0.43/config | Dump all configuration information
[**slurmdb_v0043_get_diag**](SlurmdbApi.md#slurmdb_v0043_get_diag) | **GET** /slurmdb/v0.0.43/diag/ | Get slurmdb diagnostics
[**slurmdb_v0043_get_instance**](SlurmdbApi.md#slurmdb_v0043_get_instance) | **GET** /slurmdb/v0.0.43/instance/ | Get instance info
[**slurmdb_v0043_get_instances**](SlurmdbApi.md#slurmdb_v0043_get_instances) | **GET** /slurmdb/v0.0.43/instances/ | Get instance list
[**slurmdb_v0043_get_job**](SlurmdbApi.md#slurmdb_v0043_get_job) | **GET** /slurmdb/v0.0.43/job/{job_id} | Get job info
[**slurmdb_v0043_get_jobs**](SlurmdbApi.md#slurmdb_v0043_get_jobs) | **GET** /slurmdb/v0.0.43/jobs/ | Get job list
[**slurmdb_v0043_get_ping**](SlurmdbApi.md#slurmdb_v0043_get_ping) | **GET** /slurmdb/v0.0.43/ping/ | ping test
[**slurmdb_v0043_get_qos**](SlurmdbApi.md#slurmdb_v0043_get_qos) | **GET** /slurmdb/v0.0.43/qos/ | Get QOS list
[**slurmdb_v0043_get_single_qos**](SlurmdbApi.md#slurmdb_v0043_get_single_qos) | **GET** /slurmdb/v0.0.43/qos/{qos} | Get QOS info
[**slurmdb_v0043_get_tres**](SlurmdbApi.md#slurmdb_v0043_get_tres) | **GET** /slurmdb/v0.0.43/tres/ | Get TRES info
[**slurmdb_v0043_get_user**](SlurmdbApi.md#slurmdb_v0043_get_user) | **GET** /slurmdb/v0.0.43/user/{name} | Get user info
[**slurmdb_v0043_get_users**](SlurmdbApi.md#slurmdb_v0043_get_users) | **GET** /slurmdb/v0.0.43/users/ | Get user list
[**slurmdb_v0043_get_wckey**](SlurmdbApi.md#slurmdb_v0043_get_wckey) | **GET** /slurmdb/v0.0.43/wckey/{id} | Get wckey info
[**slurmdb_v0043_get_wckeys**](SlurmdbApi.md#slurmdb_v0043_get_wckeys) | **GET** /slurmdb/v0.0.43/wckeys/ | Get wckey list
[**slurmdb_v0043_post_accounts**](SlurmdbApi.md#slurmdb_v0043_post_accounts) | **POST** /slurmdb/v0.0.43/accounts/ | Add/update list of accounts
[**slurmdb_v0043_post_accounts_association**](SlurmdbApi.md#slurmdb_v0043_post_accounts_association) | **POST** /slurmdb/v0.0.43/accounts_association/ | Add accounts with conditional association
[**slurmdb_v0043_post_associations**](SlurmdbApi.md#slurmdb_v0043_post_associations) | **POST** /slurmdb/v0.0.43/associations/ | Set associations info
[**slurmdb_v0043_post_clusters**](SlurmdbApi.md#slurmdb_v0043_post_clusters) | **POST** /slurmdb/v0.0.43/clusters/ | Get cluster list
[**slurmdb_v0043_post_config**](SlurmdbApi.md#slurmdb_v0043_post_config) | **POST** /slurmdb/v0.0.43/config | Load all configuration information
[**slurmdb_v0043_post_qos**](SlurmdbApi.md#slurmdb_v0043_post_qos) | **POST** /slurmdb/v0.0.43/qos/ | Add or update QOSs
[**slurmdb_v0043_post_tres**](SlurmdbApi.md#slurmdb_v0043_post_tres) | **POST** /slurmdb/v0.0.43/tres/ | Add TRES
[**slurmdb_v0043_post_users**](SlurmdbApi.md#slurmdb_v0043_post_users) | **POST** /slurmdb/v0.0.43/users/ | Update users
[**slurmdb_v0043_post_users_association**](SlurmdbApi.md#slurmdb_v0043_post_users_association) | **POST** /slurmdb/v0.0.43/users_association/ | Add users with conditional association
[**slurmdb_v0043_post_wckeys**](SlurmdbApi.md#slurmdb_v0043_post_wckeys) | **POST** /slurmdb/v0.0.43/wckeys/ | Add or update wckeys
[**slurmdb_v0044_delete_account**](SlurmdbApi.md#slurmdb_v0044_delete_account) | **DELETE** /slurmdb/v0.0.44/account/{account_name} | Delete account
[**slurmdb_v0044_delete_association**](SlurmdbApi.md#slurmdb_v0044_delete_association) | **DELETE** /slurmdb/v0.0.44/association/ | Delete association
[**slurmdb_v0044_delete_associations**](SlurmdbApi.md#slurmdb_v0044_delete_associations) | **DELETE** /slurmdb/v0.0.44/associations/ | Delete associations
[**slurmdb_v0044_delete_cluster**](SlurmdbApi.md#slurmdb_v0044_delete_cluster) | **DELETE** /slurmdb/v0.0.44/cluster/{cluster_name} | Delete cluster
[**slurmdb_v0044_delete_single_qos**](SlurmdbApi.md#slurmdb_v0044_delete_single_qos) | **DELETE** /slurmdb/v0.0.44/qos/{qos} | Delete QOS
[**slurmdb_v0044_delete_user**](SlurmdbApi.md#slurmdb_v0044_delete_user) | **DELETE** /slurmdb/v0.0.44/user/{name} | Delete user
[**slurmdb_v0044_delete_wckey**](SlurmdbApi.md#slurmdb_v0044_delete_wckey) | **DELETE** /slurmdb/v0.0.44/wckey/{id} | Delete wckey
[**slurmdb_v0044_get_account**](SlurmdbApi.md#slurmdb_v0044_get_account) | **GET** /slurmdb/v0.0.44/account/{account_name} | Get account info
[**slurmdb_v0044_get_accounts**](SlurmdbApi.md#slurmdb_v0044_get_accounts) | **GET** /slurmdb/v0.0.44/accounts/ | Get account list
[**slurmdb_v0044_get_association**](SlurmdbApi.md#slurmdb_v0044_get_association) | **GET** /slurmdb/v0.0.44/association/ | Get association info
[**slurmdb_v0044_get_associations**](SlurmdbApi.md#slurmdb_v0044_get_associations) | **GET** /slurmdb/v0.0.44/associations/ | Get association list
[**slurmdb_v0044_get_cluster**](SlurmdbApi.md#slurmdb_v0044_get_cluster) | **GET** /slurmdb/v0.0.44/cluster/{cluster_name} | Get cluster info
[**slurmdb_v0044_get_clusters**](SlurmdbApi.md#slurmdb_v0044_get_clusters) | **GET** /slurmdb/v0.0.44/clusters/ | Get cluster list
[**slurmdb_v0044_get_config**](SlurmdbApi.md#slurmdb_v0044_get_config) | **GET** /slurmdb/v0.0.44/config | Dump all configuration information
[**slurmdb_v0044_get_diag**](SlurmdbApi.md#slurmdb_v0044_get_diag) | **GET** /slurmdb/v0.0.44/diag/ | Get slurmdb diagnostics
[**slurmdb_v0044_get_instance**](SlurmdbApi.md#slurmdb_v0044_get_instance) | **GET** /slurmdb/v0.0.44/instance/ | Get instance info
[**slurmdb_v0044_get_instances**](SlurmdbApi.md#slurmdb_v0044_get_instances) | **GET** /slurmdb/v0.0.44/instances/ | Get instance list
[**slurmdb_v0044_get_job**](SlurmdbApi.md#slurmdb_v0044_get_job) | **GET** /slurmdb/v0.0.44/job/{job_id} | Get job info
[**slurmdb_v0044_get_jobs**](SlurmdbApi.md#slurmdb_v0044_get_jobs) | **GET** /slurmdb/v0.0.44/jobs/ | Get job list
[**slurmdb_v0044_get_ping**](SlurmdbApi.md#slurmdb_v0044_get_ping) | **GET** /slurmdb/v0.0.44/ping/ | ping test
[**slurmdb_v0044_get_qos**](SlurmdbApi.md#slurmdb_v0044_get_qos) | **GET** /slurmdb/v0.0.44/qos/ | Get QOS list
[**slurmdb_v0044_get_single_qos**](SlurmdbApi.md#slurmdb_v0044_get_single_qos) | **GET** /slurmdb/v0.0.44/qos/{qos} | Get QOS info
[**slurmdb_v0044_get_tres**](SlurmdbApi.md#slurmdb_v0044_get_tres) | **GET** /slurmdb/v0.0.44/tres/ | Get TRES info
[**slurmdb_v0044_get_user**](SlurmdbApi.md#slurmdb_v0044_get_user) | **GET** /slurmdb/v0.0.44/user/{name} | Get user info
[**slurmdb_v0044_get_users**](SlurmdbApi.md#slurmdb_v0044_get_users) | **GET** /slurmdb/v0.0.44/users/ | Get user list
[**slurmdb_v0044_get_wckey**](SlurmdbApi.md#slurmdb_v0044_get_wckey) | **GET** /slurmdb/v0.0.44/wckey/{id} | Get wckey info
[**slurmdb_v0044_get_wckeys**](SlurmdbApi.md#slurmdb_v0044_get_wckeys) | **GET** /slurmdb/v0.0.44/wckeys/ | Get wckey list
[**slurmdb_v0044_post_accounts**](SlurmdbApi.md#slurmdb_v0044_post_accounts) | **POST** /slurmdb/v0.0.44/accounts/ | Add/update list of accounts
[**slurmdb_v0044_post_accounts_association**](SlurmdbApi.md#slurmdb_v0044_post_accounts_association) | **POST** /slurmdb/v0.0.44/accounts_association/ | Add accounts with conditional association
[**slurmdb_v0044_post_associations**](SlurmdbApi.md#slurmdb_v0044_post_associations) | **POST** /slurmdb/v0.0.44/associations/ | Set associations info
[**slurmdb_v0044_post_clusters**](SlurmdbApi.md#slurmdb_v0044_post_clusters) | **POST** /slurmdb/v0.0.44/clusters/ | Get cluster list
[**slurmdb_v0044_post_config**](SlurmdbApi.md#slurmdb_v0044_post_config) | **POST** /slurmdb/v0.0.44/config | Load all configuration information
[**slurmdb_v0044_post_job**](SlurmdbApi.md#slurmdb_v0044_post_job) | **POST** /slurmdb/v0.0.44/job/{job_id} | Update job
[**slurmdb_v0044_post_jobs**](SlurmdbApi.md#slurmdb_v0044_post_jobs) | **POST** /slurmdb/v0.0.44/jobs/ | Update jobs
[**slurmdb_v0044_post_qos**](SlurmdbApi.md#slurmdb_v0044_post_qos) | **POST** /slurmdb/v0.0.44/qos/ | Add or update QOSs
[**slurmdb_v0044_post_tres**](SlurmdbApi.md#slurmdb_v0044_post_tres) | **POST** /slurmdb/v0.0.44/tres/ | Add TRES
[**slurmdb_v0044_post_users**](SlurmdbApi.md#slurmdb_v0044_post_users) | **POST** /slurmdb/v0.0.44/users/ | Update users
[**slurmdb_v0044_post_users_association**](SlurmdbApi.md#slurmdb_v0044_post_users_association) | **POST** /slurmdb/v0.0.44/users_association/ | Add users with conditional association
[**slurmdb_v0044_post_wckeys**](SlurmdbApi.md#slurmdb_v0044_post_wckeys) | **POST** /slurmdb/v0.0.44/wckeys/ | Add or update wckeys


# **slurmdb_v0041_delete_account**
> SlurmdbV0041DeleteAccount200Response slurmdb_v0041_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_delete_account200_response import SlurmdbV0041DeleteAccount200Response
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0041_delete_account(account_name)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**SlurmdbV0041DeleteAccount200Response**](SlurmdbV0041DeleteAccount200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account deletion request |  -  |
**0** | Status of account deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_association**
> V0041OpenapiAssocsRemovedResp slurmdb_v0041_delete_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_assocs_removed_resp import V0041OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | Filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | Include a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | Include sub acct information (optional)
    without_parent_info = 'without_parent_info_example' # str | Exclude parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | Exclude limits from parents (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0041_delete_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| Filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted associations | [optional] 
 **with_raw_qos** | **str**| Include a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| Include sub acct information | [optional] 
 **without_parent_info** | **str**| Exclude parent id/name | [optional] 
 **without_parent_limits** | **str**| Exclude limits from parents | [optional] 

### Return type

[**V0041OpenapiAssocsRemovedResp**](V0041OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of associations delete request |  -  |
**0** | Status of associations delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_associations**
> V0041OpenapiAssocsRemovedResp slurmdb_v0041_delete_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_assocs_removed_resp import V0041OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | Filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | Include a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | Include sub acct information (optional)
    without_parent_info = 'without_parent_info_example' # str | Exclude parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | Exclude limits from parents (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0041_delete_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| Filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted associations | [optional] 
 **with_raw_qos** | **str**| Include a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| Include sub acct information | [optional] 
 **without_parent_info** | **str**| Exclude parent id/name | [optional] 
 **without_parent_limits** | **str**| Exclude limits from parents | [optional] 

### Return type

[**V0041OpenapiAssocsRemovedResp**](V0041OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations deleted |  -  |
**0** | List of associations deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_cluster**
> SlurmdbV0041DeleteCluster200Response slurmdb_v0041_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_delete_cluster200_response import SlurmdbV0041DeleteCluster200Response
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0041_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**SlurmdbV0041DeleteCluster200Response**](SlurmdbV0041DeleteCluster200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of delete cluster request |  -  |
**0** | Result of delete cluster request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_single_qos**
> SlurmdbV0041DeleteSingleQos200Response slurmdb_v0041_delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_delete_single_qos200_response import SlurmdbV0041DeleteSingleQos200Response
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0041_delete_single_qos(qos)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**SlurmdbV0041DeleteSingleQos200Response**](SlurmdbV0041DeleteSingleQos200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_user**
> V0041OpenapiResp slurmdb_v0041_delete_user(name)

Delete user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0041_delete_user(name)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of user delete request |  -  |
**0** | Result of user delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_delete_wckey**
> SlurmdbV0041DeleteWckey200Response slurmdb_v0041_delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_delete_wckey200_response import SlurmdbV0041DeleteWckey200Response
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | wckey id

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0041_delete_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0041_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| wckey id | 

### Return type

[**SlurmdbV0041DeleteWckey200Response**](SlurmdbV0041DeleteWckey200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey deletion request |  -  |
**0** | Result of wckey deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_account**
> V0041OpenapiAccountsResp slurmdb_v0041_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_accounts_resp import V0041OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0041_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0041_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_deleted** | **str**| Include deleted | [optional] 

### Return type

[**V0041OpenapiAccountsResp**](V0041OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_accounts**
> V0041OpenapiAccountsResp slurmdb_v0041_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_accounts_resp import V0041OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    deleted = 'deleted_example' # str | include deleted associations (optional)
    with_associations = 'with_associations_example' # str | query includes associations (optional)
    with_coordinators = 'with_coordinators_example' # str | query includes coordinators (optional)
    no_users_are_coords = 'no_users_are_coords_example' # str | remove users as coordinators (optional)
    users_are_coords = 'users_are_coords_example' # str | users are coordinators (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0041_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)
        print("The response of SlurmdbApi->slurmdb_v0041_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **deleted** | **str**| include deleted associations | [optional] 
 **with_associations** | **str**| query includes associations | [optional] 
 **with_coordinators** | **str**| query includes coordinators | [optional] 
 **no_users_are_coords** | **str**| remove users as coordinators | [optional] 
 **users_are_coords** | **str**| users are coordinators | [optional] 

### Return type

[**V0041OpenapiAccountsResp**](V0041OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_association**
> V0041OpenapiAssocsResp slurmdb_v0041_get_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_assocs_resp import V0041OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | Filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | Include a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | Include sub acct information (optional)
    without_parent_info = 'without_parent_info_example' # str | Exclude parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | Exclude limits from parents (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0041_get_association(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0041_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| Filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted associations | [optional] 
 **with_raw_qos** | **str**| Include a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| Include sub acct information | [optional] 
 **without_parent_info** | **str**| Exclude parent id/name | [optional] 
 **without_parent_limits** | **str**| Exclude limits from parents | [optional] 

### Return type

[**V0041OpenapiAssocsResp**](V0041OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_associations**
> V0041OpenapiAssocsResp slurmdb_v0041_get_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_assocs_resp import V0041OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    only_defaults = 'only_defaults_example' # str | Filter to only defaults (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted associations (optional)
    with_raw_qos = 'with_raw_qos_example' # str | Include a raw qos or delta_qos (optional)
    with_sub_accts = 'with_sub_accts_example' # str | Include sub acct information (optional)
    without_parent_info = 'without_parent_info_example' # str | Exclude parent id/name (optional)
    without_parent_limits = 'without_parent_limits_example' # str | Exclude limits from parents (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0041_get_associations(account=account, cluster=cluster, default_qos=default_qos, format=format, id=id, only_defaults=only_defaults, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, with_raw_qos=with_raw_qos, with_sub_accts=with_sub_accts, without_parent_info=without_parent_info, without_parent_limits=without_parent_limits)
        print("The response of SlurmdbApi->slurmdb_v0041_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **only_defaults** | **str**| Filter to only defaults | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted associations | [optional] 
 **with_raw_qos** | **str**| Include a raw qos or delta_qos | [optional] 
 **with_sub_accts** | **str**| Include sub acct information | [optional] 
 **without_parent_info** | **str**| Exclude parent id/name | [optional] 
 **without_parent_limits** | **str**| Exclude limits from parents | [optional] 

### Return type

[**V0041OpenapiAssocsResp**](V0041OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_cluster**
> V0041OpenapiClustersResp slurmdb_v0041_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_clusters_resp import V0041OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0041_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0041_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0041OpenapiClustersResp**](V0041OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_clusters**
> V0041OpenapiClustersResp slurmdb_v0041_get_clusters(update_time=update_time)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_clusters_resp import V0041OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0041_get_clusters(update_time=update_time)
        print("The response of SlurmdbApi->slurmdb_v0041_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0041OpenapiClustersResp**](V0041OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | List of clusters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_config**
> V0041OpenapiSlurmdbdConfigResp slurmdb_v0041_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_slurmdbd_config_resp import V0041OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0041_get_config()
        print("The response of SlurmdbApi->slurmdb_v0041_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiSlurmdbdConfigResp**](V0041OpenapiSlurmdbdConfigResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_diag**
> SlurmdbV0041GetDiag200Response slurmdb_v0041_get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_get_diag200_response import SlurmdbV0041GetDiag200Response
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0041_get_diag()
        print("The response of SlurmdbApi->slurmdb_v0041_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlurmdbV0041GetDiag200Response**](SlurmdbV0041GetDiag200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_instance**
> V0041OpenapiInstancesResp slurmdb_v0041_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_instances_resp import V0041OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance info
        api_response = api_instance.slurmdb_v0041_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0041_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0041OpenapiInstancesResp**](V0041OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_instances**
> V0041OpenapiInstancesResp slurmdb_v0041_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_instances_resp import V0041OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance list
        api_response = api_instance.slurmdb_v0041_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0041_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0041OpenapiInstancesResp**](V0041OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_job**
> V0041OpenapiSlurmdbdJobsResp slurmdb_v0041_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_slurmdbd_jobs_resp import V0041OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job id

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0041_get_job(job_id)
        print("The response of SlurmdbApi->slurmdb_v0041_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job id | 

### Return type

[**V0041OpenapiSlurmdbdJobsResp**](V0041OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Job description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_jobs**
> V0041OpenapiSlurmdbdJobsResp slurmdb_v0041_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_slurmdbd_jobs_resp import V0041OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    scheduler_unset = 'scheduler_unset_example' # str | Schedule bits not set (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str | Job was started on submit (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str | Job was started from main scheduler (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str | Job was started from backfill (optional)
    job_started = 'job_started_example' # str | Job start RPC was received (optional)
    exit_code = 'exit_code_example' # str | Job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str | Include duplicate job entries (optional)
    skip_steps = 'skip_steps_example' # str | Exclude job step details (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str | Do not truncate the time to usage_start and usage_end (optional)
    whole_hetjob = 'whole_hetjob_example' # str | Include details on all hetjob components (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str | Only show details on specified hetjob components (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str | Tell dbd not to wait for the result (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str | Use usage_time as the submit_time of the job (optional)
    show_batch_script = 'show_batch_script_example' # str | Include job script (optional)
    show_job_environment = 'show_job_environment_example' # str | Include job environment (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    end_time = 'end_time_example' # str | Usage end (UNIX timestamp) (optional)
    start_time = 'start_time_example' # str | Usage start (UNIX timestamp) (optional)
    node = 'node_example' # str | Ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV wckey list (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0041_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->slurmdb_v0041_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **scheduler_unset** | **str**| Schedule bits not set | [optional] 
 **scheduled_on_submit** | **str**| Job was started on submit | [optional] 
 **scheduled_by_main** | **str**| Job was started from main scheduler | [optional] 
 **scheduled_by_backfill** | **str**| Job was started from backfill | [optional] 
 **job_started** | **str**| Job start RPC was received | [optional] 
 **exit_code** | **str**| Job exit code (numeric) | [optional] 
 **show_duplicates** | **str**| Include duplicate job entries | [optional] 
 **skip_steps** | **str**| Exclude job step details | [optional] 
 **disable_truncate_usage_time** | **str**| Do not truncate the time to usage_start and usage_end | [optional] 
 **whole_hetjob** | **str**| Include details on all hetjob components | [optional] 
 **disable_whole_hetjob** | **str**| Only show details on specified hetjob components | [optional] 
 **disable_wait_for_result** | **str**| Tell dbd not to wait for the result | [optional] 
 **usage_time_as_submit_time** | **str**| Use usage_time as the submit_time of the job | [optional] 
 **show_batch_script** | **str**| Include job script | [optional] 
 **show_job_environment** | **str**| Include job environment | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **end_time** | **str**| Usage end (UNIX timestamp) | [optional] 
 **start_time** | **str**| Usage start (UNIX timestamp) | [optional] 
 **node** | **str**| Ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV wckey list | [optional] 

### Return type

[**V0041OpenapiSlurmdbdJobsResp**](V0041OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | List of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_qos**
> V0041OpenapiSlurmdbdQosResp slurmdb_v0041_get_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted)

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted QOS (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0041_get_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0041_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **with_deleted** | **str**| Include deleted QOS | [optional] 

### Return type

[**V0041OpenapiSlurmdbdQosResp**](V0041OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS |  -  |
**0** | List of QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_single_qos**
> V0041OpenapiSlurmdbdQosResp slurmdb_v0041_get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0041_get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0041_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**V0041OpenapiSlurmdbdQosResp**](V0041OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_tres**
> V0041OpenapiTresResp slurmdb_v0041_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_tres_resp import V0041OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0041_get_tres()
        print("The response of SlurmdbApi->slurmdb_v0041_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiTresResp**](V0041OpenapiTresResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | List of TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_user**
> V0041OpenapiUsersResp slurmdb_v0041_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_users_resp import V0041OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include wckeys (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0041_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->slurmdb_v0041_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include wckeys | [optional] 

### Return type

[**V0041OpenapiUsersResp**](V0041OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_users**
> V0041OpenapiUsersResp slurmdb_v0041_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_users_resp import V0041OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default wckey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With wckeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0041_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->slurmdb_v0041_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default wckey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With wckeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**V0041OpenapiUsersResp**](V0041OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_wckey**
> V0041OpenapiWckeyResp slurmdb_v0041_get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_wckey_resp import V0041OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | wckey id

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0041_get_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0041_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| wckey id | 

### Return type

[**V0041OpenapiWckeyResp**](V0041OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Description of wckey |  -  |
**0** | Description of wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_get_wckeys**
> V0041OpenapiWckeyResp slurmdb_v0041_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_wckey_resp import V0041OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted wckeys (optional)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0041_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0041_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted wckeys | [optional] 

### Return type

[**V0041OpenapiWckeyResp**](V0041OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | List of wckeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_accounts**
> V0041OpenapiResp slurmdb_v0041_post_accounts(v0041_openapi_accounts_resp=v0041_openapi_accounts_resp)

Add/update list of accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_accounts_resp import V0041OpenapiAccountsResp
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0041_openapi_accounts_resp = slurmrestapi.V0041OpenapiAccountsResp() # V0041OpenapiAccountsResp | Description of accounts to update/create (optional)

    try:
        # Add/update list of accounts
        api_response = api_instance.slurmdb_v0041_post_accounts(v0041_openapi_accounts_resp=v0041_openapi_accounts_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_openapi_accounts_resp** | [**V0041OpenapiAccountsResp**](V0041OpenapiAccountsResp.md)| Description of accounts to update/create | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account update request |  -  |
**0** | Status of account update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_accounts_association**
> SlurmdbV0041PostAccountsAssociation200Response slurmdb_v0041_post_accounts_association(slurmdb_v0041_post_accounts_association_request=slurmdb_v0041_post_accounts_association_request)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_post_accounts_association200_response import SlurmdbV0041PostAccountsAssociation200Response
from slurmrestapi.models.slurmdb_v0041_post_accounts_association_request import SlurmdbV0041PostAccountsAssociationRequest
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    slurmdb_v0041_post_accounts_association_request = slurmrestapi.SlurmdbV0041PostAccountsAssociationRequest() # SlurmdbV0041PostAccountsAssociationRequest | Add list of accounts with conditional association (optional)

    try:
        # Add accounts with conditional association
        api_response = api_instance.slurmdb_v0041_post_accounts_association(slurmdb_v0041_post_accounts_association_request=slurmdb_v0041_post_accounts_association_request)
        print("The response of SlurmdbApi->slurmdb_v0041_post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slurmdb_v0041_post_accounts_association_request** | [**SlurmdbV0041PostAccountsAssociationRequest**](SlurmdbV0041PostAccountsAssociationRequest.md)| Add list of accounts with conditional association | [optional] 

### Return type

[**SlurmdbV0041PostAccountsAssociation200Response**](SlurmdbV0041PostAccountsAssociation200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account addition request |  -  |
**0** | Status of account addition request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_associations**
> V0041OpenapiResp slurmdb_v0041_post_associations(v0041_openapi_assocs_resp=v0041_openapi_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_assocs_resp import V0041OpenapiAssocsResp
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0041_openapi_assocs_resp = slurmrestapi.V0041OpenapiAssocsResp() # V0041OpenapiAssocsResp | Job description (optional)

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0041_post_associations(v0041_openapi_assocs_resp=v0041_openapi_assocs_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_openapi_assocs_resp** | [**V0041OpenapiAssocsResp**](V0041OpenapiAssocsResp.md)| Job description | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | status of associations update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_clusters**
> V0041OpenapiResp slurmdb_v0041_post_clusters(update_time=update_time, v0041_openapi_clusters_resp=v0041_openapi_clusters_resp)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_clusters_resp import V0041OpenapiClustersResp
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)
    v0041_openapi_clusters_resp = slurmrestapi.V0041OpenapiClustersResp() # V0041OpenapiClustersResp | Cluster add or update descriptions (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0041_post_clusters(update_time=update_time, v0041_openapi_clusters_resp=v0041_openapi_clusters_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 
 **v0041_openapi_clusters_resp** | [**V0041OpenapiClustersResp**](V0041OpenapiClustersResp.md)| Cluster add or update descriptions | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of modify clusters request |  -  |
**0** | Result of modify clusters request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_config**
> V0041OpenapiResp slurmdb_v0041_post_config(v0041_openapi_slurmdbd_config_resp=v0041_openapi_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.models.v0041_openapi_slurmdbd_config_resp import V0041OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0041_openapi_slurmdbd_config_resp = slurmrestapi.V0041OpenapiSlurmdbdConfigResp() # V0041OpenapiSlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0041_post_config(v0041_openapi_slurmdbd_config_resp=v0041_openapi_slurmdbd_config_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_openapi_slurmdbd_config_resp** | [**V0041OpenapiSlurmdbdConfigResp**](V0041OpenapiSlurmdbdConfigResp.md)| Add or update config | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_qos**
> V0041OpenapiResp slurmdb_v0041_post_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted, v0041_openapi_slurmdbd_qos_resp=v0041_openapi_slurmdbd_qos_resp)

Add or update QOSs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted QOS (optional)
    v0041_openapi_slurmdbd_qos_resp = slurmrestapi.V0041OpenapiSlurmdbdQosResp() # V0041OpenapiSlurmdbdQosResp | Description of QOS to add or update (optional)

    try:
        # Add or update QOSs
        api_response = api_instance.slurmdb_v0041_post_qos(description=description, id=id, format=format, name=name, preempt_mode=preempt_mode, with_deleted=with_deleted, v0041_openapi_slurmdbd_qos_resp=v0041_openapi_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **with_deleted** | **str**| Include deleted QOS | [optional] 
 **v0041_openapi_slurmdbd_qos_resp** | [**V0041OpenapiSlurmdbdQosResp**](V0041OpenapiSlurmdbdQosResp.md)| Description of QOS to add or update | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | QOS update response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_tres**
> V0041OpenapiResp slurmdb_v0041_post_tres(v0041_openapi_tres_resp=v0041_openapi_tres_resp)

Add TRES

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.models.v0041_openapi_tres_resp import V0041OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0041_openapi_tres_resp = slurmrestapi.V0041OpenapiTresResp() # V0041OpenapiTresResp | TRES descriptions. Only works in developer mode. (optional)

    try:
        # Add TRES
        api_response = api_instance.slurmdb_v0041_post_tres(v0041_openapi_tres_resp=v0041_openapi_tres_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_openapi_tres_resp** | [**V0041OpenapiTresResp**](V0041OpenapiTresResp.md)| TRES descriptions. Only works in developer mode. | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TRES update result |  -  |
**0** | TRES update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_users**
> V0041OpenapiResp slurmdb_v0041_post_users(v0041_openapi_users_resp=v0041_openapi_users_resp)

Update users

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.models.v0041_openapi_users_resp import V0041OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0041_openapi_users_resp = slurmrestapi.V0041OpenapiUsersResp() # V0041OpenapiUsersResp | add or update user (optional)

    try:
        # Update users
        api_response = api_instance.slurmdb_v0041_post_users(v0041_openapi_users_resp=v0041_openapi_users_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_openapi_users_resp** | [**V0041OpenapiUsersResp**](V0041OpenapiUsersResp.md)| add or update user | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of user update request |  -  |
**0** | Status of user update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_users_association**
> SlurmdbV0041PostUsersAssociation200Response slurmdb_v0041_post_users_association(update_time=update_time, flags=flags, slurmdb_v0041_post_users_association_request=slurmdb_v0041_post_users_association_request)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.slurmdb_v0041_post_users_association200_response import SlurmdbV0041PostUsersAssociation200Response
from slurmrestapi.models.slurmdb_v0041_post_users_association_request import SlurmdbV0041PostUsersAssociationRequest
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)
    slurmdb_v0041_post_users_association_request = slurmrestapi.SlurmdbV0041PostUsersAssociationRequest() # SlurmdbV0041PostUsersAssociationRequest | Create users with conditional association (optional)

    try:
        # Add users with conditional association
        api_response = api_instance.slurmdb_v0041_post_users_association(update_time=update_time, flags=flags, slurmdb_v0041_post_users_association_request=slurmdb_v0041_post_users_association_request)
        print("The response of SlurmdbApi->slurmdb_v0041_post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **slurmdb_v0041_post_users_association_request** | [**SlurmdbV0041PostUsersAssociationRequest**](SlurmdbV0041PostUsersAssociationRequest.md)| Create users with conditional association | [optional] 

### Return type

[**SlurmdbV0041PostUsersAssociation200Response**](SlurmdbV0041PostUsersAssociation200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Add list of users with conditional association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0041_post_wckeys**
> V0041OpenapiResp slurmdb_v0041_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0041_openapi_wckey_resp=v0041_openapi_wckey_resp)

Add or update wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrestapi.models.v0041_openapi_wckey_resp import V0041OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV id list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted wckeys (optional)
    v0041_openapi_wckey_resp = slurmrestapi.V0041OpenapiWckeyResp() # V0041OpenapiWckeyResp | wckeys description (optional)

    try:
        # Add or update wckeys
        api_response = api_instance.slurmdb_v0041_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0041_openapi_wckey_resp=v0041_openapi_wckey_resp)
        print("The response of SlurmdbApi->slurmdb_v0041_post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0041_post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV id list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted wckeys | [optional] 
 **v0041_openapi_wckey_resp** | [**V0041OpenapiWckeyResp**](V0041OpenapiWckeyResp.md)| wckeys description | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey addition or update request |  -  |
**0** | Result of wckey addition or update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_account**
> V0042OpenapiAccountsRemovedResp slurmdb_v0042_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_accounts_removed_resp import V0042OpenapiAccountsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0042_delete_account(account_name)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**V0042OpenapiAccountsRemovedResp**](V0042OpenapiAccountsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account deletion request |  -  |
**0** | Status of account deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_association**
> V0042OpenapiAssocsRemovedResp slurmdb_v0042_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_assocs_removed_resp import V0042OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0042_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0042OpenapiAssocsRemovedResp**](V0042OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of associations delete request |  -  |
**0** | Status of associations delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_associations**
> V0042OpenapiAssocsRemovedResp slurmdb_v0042_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_assocs_removed_resp import V0042OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0042_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0042OpenapiAssocsRemovedResp**](V0042OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations deleted |  -  |
**0** | List of associations deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_cluster**
> V0042OpenapiClustersRemovedResp slurmdb_v0042_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_clusters_removed_resp import V0042OpenapiClustersRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0042_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0042OpenapiClustersRemovedResp**](V0042OpenapiClustersRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of delete cluster request |  -  |
**0** | Result of delete cluster request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_single_qos**
> V0042OpenapiSlurmdbdQosRemovedResp slurmdb_v0042_delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_qos_removed_resp import V0042OpenapiSlurmdbdQosRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0042_delete_single_qos(qos)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**V0042OpenapiSlurmdbdQosRemovedResp**](V0042OpenapiSlurmdbdQosRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_user**
> V0042OpenapiResp slurmdb_v0042_delete_user(name)

Delete user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0042_delete_user(name)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of user delete request |  -  |
**0** | Result of user delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_delete_wckey**
> V0042OpenapiWckeyRemovedResp slurmdb_v0042_delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_wckey_removed_resp import V0042OpenapiWckeyRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0042_delete_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0042_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0042OpenapiWckeyRemovedResp**](V0042OpenapiWckeyRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey deletion request |  -  |
**0** | Result of wckey deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_account**
> V0042OpenapiAccountsResp slurmdb_v0042_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_accounts_resp import V0042OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0042_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0042_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_deleted** | **str**| Include deleted | [optional] 

### Return type

[**V0042OpenapiAccountsResp**](V0042OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_accounts**
> V0042OpenapiAccountsResp slurmdb_v0042_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_accounts_resp import V0042OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    deleted = 'deleted_example' # str | include deleted associations (optional)
    with_associations = 'with_associations_example' # str | query includes associations (optional)
    with_coordinators = 'with_coordinators_example' # str | query includes coordinators (optional)
    no_users_are_coords = 'no_users_are_coords_example' # str | remove users as coordinators (optional)
    users_are_coords = 'users_are_coords_example' # str | users are coordinators (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0042_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)
        print("The response of SlurmdbApi->slurmdb_v0042_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **deleted** | **str**| include deleted associations | [optional] 
 **with_associations** | **str**| query includes associations | [optional] 
 **with_coordinators** | **str**| query includes coordinators | [optional] 
 **no_users_are_coords** | **str**| remove users as coordinators | [optional] 
 **users_are_coords** | **str**| users are coordinators | [optional] 

### Return type

[**V0042OpenapiAccountsResp**](V0042OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_association**
> V0042OpenapiAssocsResp slurmdb_v0042_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_assocs_resp import V0042OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0042_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0042_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0042OpenapiAssocsResp**](V0042OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_associations**
> V0042OpenapiAssocsResp slurmdb_v0042_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_assocs_resp import V0042OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0042_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0042_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0042OpenapiAssocsResp**](V0042OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_cluster**
> V0042OpenapiClustersResp slurmdb_v0042_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_clusters_resp import V0042OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0042_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0042_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0042OpenapiClustersResp**](V0042OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_clusters**
> V0042OpenapiClustersResp slurmdb_v0042_get_clusters(update_time=update_time)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_clusters_resp import V0042OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0042_get_clusters(update_time=update_time)
        print("The response of SlurmdbApi->slurmdb_v0042_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**V0042OpenapiClustersResp**](V0042OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | List of clusters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_config**
> V0042OpenapiSlurmdbdConfigResp slurmdb_v0042_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_config_resp import V0042OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0042_get_config()
        print("The response of SlurmdbApi->slurmdb_v0042_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0042OpenapiSlurmdbdConfigResp**](V0042OpenapiSlurmdbdConfigResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_diag**
> V0042OpenapiSlurmdbdStatsResp slurmdb_v0042_get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_stats_resp import V0042OpenapiSlurmdbdStatsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0042_get_diag()
        print("The response of SlurmdbApi->slurmdb_v0042_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0042OpenapiSlurmdbdStatsResp**](V0042OpenapiSlurmdbdStatsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_instance**
> V0042OpenapiInstancesResp slurmdb_v0042_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_instances_resp import V0042OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance info
        api_response = api_instance.slurmdb_v0042_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0042_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0042OpenapiInstancesResp**](V0042OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_instances**
> V0042OpenapiInstancesResp slurmdb_v0042_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_instances_resp import V0042OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance list
        api_response = api_instance.slurmdb_v0042_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0042_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0042OpenapiInstancesResp**](V0042OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_job**
> V0042OpenapiSlurmdbdJobsResp slurmdb_v0042_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_jobs_resp import V0042OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0042_get_job(job_id)
        print("The response of SlurmdbApi->slurmdb_v0042_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**V0042OpenapiSlurmdbdJobsResp**](V0042OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Job description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_jobs**
> V0042OpenapiSlurmdbdJobsResp slurmdb_v0042_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_jobs_resp import V0042OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    scheduler_unset = 'scheduler_unset_example' # str | Schedule bits not set (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str | Job was started on submit (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str | Job was started from main scheduler (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str | Job was started from backfill (optional)
    job_started = 'job_started_example' # str | Job start RPC was received (optional)
    exit_code = 'exit_code_example' # str | Job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str | Include duplicate job entries (optional)
    skip_steps = 'skip_steps_example' # str | Exclude job step details (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str | Do not truncate the time to usage_start and usage_end (optional)
    whole_hetjob = 'whole_hetjob_example' # str | Include details on all hetjob components (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str | Only show details on specified hetjob components (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str | Tell dbd not to wait for the result (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str | Use usage_time as the submit_time of the job (optional)
    show_batch_script = 'show_batch_script_example' # str | Include job script (optional)
    show_job_environment = 'show_job_environment_example' # str | Include job environment (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    end_time = 'end_time_example' # str | Usage end (UNIX timestamp) (optional)
    start_time = 'start_time_example' # str | Usage start (UNIX timestamp) (optional)
    node = 'node_example' # str | Ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV WCKey list (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0042_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->slurmdb_v0042_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **scheduler_unset** | **str**| Schedule bits not set | [optional] 
 **scheduled_on_submit** | **str**| Job was started on submit | [optional] 
 **scheduled_by_main** | **str**| Job was started from main scheduler | [optional] 
 **scheduled_by_backfill** | **str**| Job was started from backfill | [optional] 
 **job_started** | **str**| Job start RPC was received | [optional] 
 **exit_code** | **str**| Job exit code (numeric) | [optional] 
 **show_duplicates** | **str**| Include duplicate job entries | [optional] 
 **skip_steps** | **str**| Exclude job step details | [optional] 
 **disable_truncate_usage_time** | **str**| Do not truncate the time to usage_start and usage_end | [optional] 
 **whole_hetjob** | **str**| Include details on all hetjob components | [optional] 
 **disable_whole_hetjob** | **str**| Only show details on specified hetjob components | [optional] 
 **disable_wait_for_result** | **str**| Tell dbd not to wait for the result | [optional] 
 **usage_time_as_submit_time** | **str**| Use usage_time as the submit_time of the job | [optional] 
 **show_batch_script** | **str**| Include job script | [optional] 
 **show_job_environment** | **str**| Include job environment | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **end_time** | **str**| Usage end (UNIX timestamp) | [optional] 
 **start_time** | **str**| Usage start (UNIX timestamp) | [optional] 
 **node** | **str**| Ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV WCKey list | [optional] 

### Return type

[**V0042OpenapiSlurmdbdJobsResp**](V0042OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | List of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_ping**
> V0042OpenapiSlurmdbdPingResp slurmdb_v0042_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_ping_resp import V0042OpenapiSlurmdbdPingResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurmdb_v0042_get_ping()
        print("The response of SlurmdbApi->slurmdb_v0042_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0042OpenapiSlurmdbdPingResp**](V0042OpenapiSlurmdbdPingResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_qos**
> V0042OpenapiSlurmdbdQosResp slurmdb_v0042_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_qos_resp import V0042OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0042_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)
        print("The response of SlurmdbApi->slurmdb_v0042_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 

### Return type

[**V0042OpenapiSlurmdbdQosResp**](V0042OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS |  -  |
**0** | List of QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_single_qos**
> V0042OpenapiSlurmdbdQosResp slurmdb_v0042_get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_slurmdbd_qos_resp import V0042OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0042_get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0042_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**V0042OpenapiSlurmdbdQosResp**](V0042OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_tres**
> V0042OpenapiTresResp slurmdb_v0042_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_tres_resp import V0042OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0042_get_tres()
        print("The response of SlurmdbApi->slurmdb_v0042_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0042OpenapiTresResp**](V0042OpenapiTresResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | List of TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_user**
> V0042OpenapiUsersResp slurmdb_v0042_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_users_resp import V0042OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include WCKeys (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0042_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->slurmdb_v0042_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include WCKeys | [optional] 

### Return type

[**V0042OpenapiUsersResp**](V0042OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_users**
> V0042OpenapiUsersResp slurmdb_v0042_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_users_resp import V0042OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default WCKey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With WCKeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0042_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->slurmdb_v0042_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default WCKey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With WCKeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**V0042OpenapiUsersResp**](V0042OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_wckey**
> V0042OpenapiWckeyResp slurmdb_v0042_get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_wckey_resp import V0042OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0042_get_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0042_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0042OpenapiWckeyResp**](V0042OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Description of wckey |  -  |
**0** | Description of wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_get_wckeys**
> V0042OpenapiWckeyResp slurmdb_v0042_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_wckey_resp import V0042OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0042_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0042_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 

### Return type

[**V0042OpenapiWckeyResp**](V0042OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | List of wckeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_accounts**
> V0042OpenapiResp slurmdb_v0042_post_accounts(v0042_openapi_accounts_resp=v0042_openapi_accounts_resp)

Add/update list of accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_accounts_resp import V0042OpenapiAccountsResp
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_accounts_resp = slurmrestapi.V0042OpenapiAccountsResp() # V0042OpenapiAccountsResp | Description of accounts to update/create (optional)

    try:
        # Add/update list of accounts
        api_response = api_instance.slurmdb_v0042_post_accounts(v0042_openapi_accounts_resp=v0042_openapi_accounts_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_accounts_resp** | [**V0042OpenapiAccountsResp**](V0042OpenapiAccountsResp.md)| Description of accounts to update/create | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account update request |  -  |
**0** | Status of account update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_accounts_association**
> V0042OpenapiAccountsAddCondRespStr slurmdb_v0042_post_accounts_association(v0042_openapi_accounts_add_cond_resp=v0042_openapi_accounts_add_cond_resp)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_accounts_add_cond_resp import V0042OpenapiAccountsAddCondResp
from slurmrestapi.models.v0042_openapi_accounts_add_cond_resp_str import V0042OpenapiAccountsAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_accounts_add_cond_resp = slurmrestapi.V0042OpenapiAccountsAddCondResp() # V0042OpenapiAccountsAddCondResp | Add list of accounts with conditional association (optional)

    try:
        # Add accounts with conditional association
        api_response = api_instance.slurmdb_v0042_post_accounts_association(v0042_openapi_accounts_add_cond_resp=v0042_openapi_accounts_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_accounts_add_cond_resp** | [**V0042OpenapiAccountsAddCondResp**](V0042OpenapiAccountsAddCondResp.md)| Add list of accounts with conditional association | [optional] 

### Return type

[**V0042OpenapiAccountsAddCondRespStr**](V0042OpenapiAccountsAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account addition request |  -  |
**0** | Status of account addition request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_associations**
> V0042OpenapiResp slurmdb_v0042_post_associations(v0042_openapi_assocs_resp=v0042_openapi_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_assocs_resp import V0042OpenapiAssocsResp
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_assocs_resp = slurmrestapi.V0042OpenapiAssocsResp() # V0042OpenapiAssocsResp | Job description (optional)

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0042_post_associations(v0042_openapi_assocs_resp=v0042_openapi_assocs_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_assocs_resp** | [**V0042OpenapiAssocsResp**](V0042OpenapiAssocsResp.md)| Job description | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | status of associations update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_clusters**
> V0042OpenapiResp slurmdb_v0042_post_clusters(update_time=update_time, v0042_openapi_clusters_resp=v0042_openapi_clusters_resp)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_clusters_resp import V0042OpenapiClustersResp
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)
    v0042_openapi_clusters_resp = slurmrestapi.V0042OpenapiClustersResp() # V0042OpenapiClustersResp | Cluster add or update descriptions (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0042_post_clusters(update_time=update_time, v0042_openapi_clusters_resp=v0042_openapi_clusters_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 
 **v0042_openapi_clusters_resp** | [**V0042OpenapiClustersResp**](V0042OpenapiClustersResp.md)| Cluster add or update descriptions | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of modify clusters request |  -  |
**0** | Result of modify clusters request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_config**
> V0042OpenapiResp slurmdb_v0042_post_config(v0042_openapi_slurmdbd_config_resp=v0042_openapi_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.models.v0042_openapi_slurmdbd_config_resp import V0042OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_slurmdbd_config_resp = slurmrestapi.V0042OpenapiSlurmdbdConfigResp() # V0042OpenapiSlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0042_post_config(v0042_openapi_slurmdbd_config_resp=v0042_openapi_slurmdbd_config_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_slurmdbd_config_resp** | [**V0042OpenapiSlurmdbdConfigResp**](V0042OpenapiSlurmdbdConfigResp.md)| Add or update config | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_qos**
> V0042OpenapiResp slurmdb_v0042_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0042_openapi_slurmdbd_qos_resp=v0042_openapi_slurmdbd_qos_resp)

Add or update QOSs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.models.v0042_openapi_slurmdbd_qos_resp import V0042OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    v0042_openapi_slurmdbd_qos_resp = slurmrestapi.V0042OpenapiSlurmdbdQosResp() # V0042OpenapiSlurmdbdQosResp | Description of QOS to add or update (optional)

    try:
        # Add or update QOSs
        api_response = api_instance.slurmdb_v0042_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0042_openapi_slurmdbd_qos_resp=v0042_openapi_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **v0042_openapi_slurmdbd_qos_resp** | [**V0042OpenapiSlurmdbdQosResp**](V0042OpenapiSlurmdbdQosResp.md)| Description of QOS to add or update | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | QOS update response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_tres**
> V0042OpenapiResp slurmdb_v0042_post_tres(v0042_openapi_tres_resp=v0042_openapi_tres_resp)

Add TRES

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.models.v0042_openapi_tres_resp import V0042OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_tres_resp = slurmrestapi.V0042OpenapiTresResp() # V0042OpenapiTresResp | TRES descriptions. Only works in developer mode. (optional)

    try:
        # Add TRES
        api_response = api_instance.slurmdb_v0042_post_tres(v0042_openapi_tres_resp=v0042_openapi_tres_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_tres_resp** | [**V0042OpenapiTresResp**](V0042OpenapiTresResp.md)| TRES descriptions. Only works in developer mode. | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TRES update result |  -  |
**0** | TRES update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_users**
> V0042OpenapiResp slurmdb_v0042_post_users(v0042_openapi_users_resp=v0042_openapi_users_resp)

Update users

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.models.v0042_openapi_users_resp import V0042OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0042_openapi_users_resp = slurmrestapi.V0042OpenapiUsersResp() # V0042OpenapiUsersResp | add or update user (optional)

    try:
        # Update users
        api_response = api_instance.slurmdb_v0042_post_users(v0042_openapi_users_resp=v0042_openapi_users_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0042_openapi_users_resp** | [**V0042OpenapiUsersResp**](V0042OpenapiUsersResp.md)| add or update user | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of user update request |  -  |
**0** | Status of user update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_users_association**
> V0042OpenapiUsersAddCondRespStr slurmdb_v0042_post_users_association(update_time=update_time, flags=flags, v0042_openapi_users_add_cond_resp=v0042_openapi_users_add_cond_resp)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_users_add_cond_resp import V0042OpenapiUsersAddCondResp
from slurmrestapi.models.v0042_openapi_users_add_cond_resp_str import V0042OpenapiUsersAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)
    v0042_openapi_users_add_cond_resp = slurmrestapi.V0042OpenapiUsersAddCondResp() # V0042OpenapiUsersAddCondResp | Create users with conditional association (optional)

    try:
        # Add users with conditional association
        api_response = api_instance.slurmdb_v0042_post_users_association(update_time=update_time, flags=flags, v0042_openapi_users_add_cond_resp=v0042_openapi_users_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **v0042_openapi_users_add_cond_resp** | [**V0042OpenapiUsersAddCondResp**](V0042OpenapiUsersAddCondResp.md)| Create users with conditional association | [optional] 

### Return type

[**V0042OpenapiUsersAddCondRespStr**](V0042OpenapiUsersAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Add list of users with conditional association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0042_post_wckeys**
> V0042OpenapiResp slurmdb_v0042_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0042_openapi_wckey_resp=v0042_openapi_wckey_resp)

Add or update wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0042_openapi_resp import V0042OpenapiResp
from slurmrestapi.models.v0042_openapi_wckey_resp import V0042OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)
    v0042_openapi_wckey_resp = slurmrestapi.V0042OpenapiWckeyResp() # V0042OpenapiWckeyResp | wckeys description (optional)

    try:
        # Add or update wckeys
        api_response = api_instance.slurmdb_v0042_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0042_openapi_wckey_resp=v0042_openapi_wckey_resp)
        print("The response of SlurmdbApi->slurmdb_v0042_post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0042_post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 
 **v0042_openapi_wckey_resp** | [**V0042OpenapiWckeyResp**](V0042OpenapiWckeyResp.md)| wckeys description | [optional] 

### Return type

[**V0042OpenapiResp**](V0042OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey addition or update request |  -  |
**0** | Result of wckey addition or update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_account**
> V0043OpenapiAccountsRemovedResp slurmdb_v0043_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_accounts_removed_resp import V0043OpenapiAccountsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0043_delete_account(account_name)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**V0043OpenapiAccountsRemovedResp**](V0043OpenapiAccountsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account deletion request |  -  |
**0** | Status of account deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_association**
> V0043OpenapiAssocsRemovedResp slurmdb_v0043_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_assocs_removed_resp import V0043OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0043_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0043OpenapiAssocsRemovedResp**](V0043OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of associations delete request |  -  |
**0** | Status of associations delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_associations**
> V0043OpenapiAssocsRemovedResp slurmdb_v0043_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_assocs_removed_resp import V0043OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0043_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0043OpenapiAssocsRemovedResp**](V0043OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations deleted |  -  |
**0** | List of associations deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_cluster**
> V0043OpenapiClustersRemovedResp slurmdb_v0043_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_clusters_removed_resp import V0043OpenapiClustersRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0043_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0043OpenapiClustersRemovedResp**](V0043OpenapiClustersRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of delete cluster request |  -  |
**0** | Result of delete cluster request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_single_qos**
> V0043OpenapiSlurmdbdQosRemovedResp slurmdb_v0043_delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_qos_removed_resp import V0043OpenapiSlurmdbdQosRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0043_delete_single_qos(qos)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**V0043OpenapiSlurmdbdQosRemovedResp**](V0043OpenapiSlurmdbdQosRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_user**
> V0043OpenapiResp slurmdb_v0043_delete_user(name)

Delete user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0043_delete_user(name)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of user delete request |  -  |
**0** | Result of user delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_delete_wckey**
> V0043OpenapiWckeyRemovedResp slurmdb_v0043_delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_wckey_removed_resp import V0043OpenapiWckeyRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0043_delete_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0043_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0043OpenapiWckeyRemovedResp**](V0043OpenapiWckeyRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey deletion request |  -  |
**0** | Result of wckey deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_account**
> V0043OpenapiAccountsResp slurmdb_v0043_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_accounts_resp import V0043OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0043_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0043_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_deleted** | **str**| Include deleted | [optional] 

### Return type

[**V0043OpenapiAccountsResp**](V0043OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_accounts**
> V0043OpenapiAccountsResp slurmdb_v0043_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_accounts_resp import V0043OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    deleted = 'deleted_example' # str | include deleted associations (optional)
    with_associations = 'with_associations_example' # str | query includes associations (optional)
    with_coordinators = 'with_coordinators_example' # str | query includes coordinators (optional)
    no_users_are_coords = 'no_users_are_coords_example' # str | remove users as coordinators (optional)
    users_are_coords = 'users_are_coords_example' # str | users are coordinators (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0043_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)
        print("The response of SlurmdbApi->slurmdb_v0043_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **deleted** | **str**| include deleted associations | [optional] 
 **with_associations** | **str**| query includes associations | [optional] 
 **with_coordinators** | **str**| query includes coordinators | [optional] 
 **no_users_are_coords** | **str**| remove users as coordinators | [optional] 
 **users_are_coords** | **str**| users are coordinators | [optional] 

### Return type

[**V0043OpenapiAccountsResp**](V0043OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_association**
> V0043OpenapiAssocsResp slurmdb_v0043_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_assocs_resp import V0043OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0043_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0043_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0043OpenapiAssocsResp**](V0043OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_associations**
> V0043OpenapiAssocsResp slurmdb_v0043_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_assocs_resp import V0043OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0043_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0043_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0043OpenapiAssocsResp**](V0043OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_cluster**
> V0043OpenapiClustersResp slurmdb_v0043_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_clusters_resp import V0043OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0043_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0043_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0043OpenapiClustersResp**](V0043OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_clusters**
> V0043OpenapiClustersResp slurmdb_v0043_get_clusters(update_time=update_time)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_clusters_resp import V0043OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0043_get_clusters(update_time=update_time)
        print("The response of SlurmdbApi->slurmdb_v0043_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**V0043OpenapiClustersResp**](V0043OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | List of clusters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_config**
> V0043OpenapiSlurmdbdConfigResp slurmdb_v0043_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_config_resp import V0043OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0043_get_config()
        print("The response of SlurmdbApi->slurmdb_v0043_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0043OpenapiSlurmdbdConfigResp**](V0043OpenapiSlurmdbdConfigResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_diag**
> V0043OpenapiSlurmdbdStatsResp slurmdb_v0043_get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_stats_resp import V0043OpenapiSlurmdbdStatsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0043_get_diag()
        print("The response of SlurmdbApi->slurmdb_v0043_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0043OpenapiSlurmdbdStatsResp**](V0043OpenapiSlurmdbdStatsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_instance**
> V0043OpenapiInstancesResp slurmdb_v0043_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_instances_resp import V0043OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance info
        api_response = api_instance.slurmdb_v0043_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0043_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0043OpenapiInstancesResp**](V0043OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_instances**
> V0043OpenapiInstancesResp slurmdb_v0043_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_instances_resp import V0043OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance list
        api_response = api_instance.slurmdb_v0043_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0043_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0043OpenapiInstancesResp**](V0043OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_job**
> V0043OpenapiSlurmdbdJobsResp slurmdb_v0043_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_jobs_resp import V0043OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0043_get_job(job_id)
        print("The response of SlurmdbApi->slurmdb_v0043_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**V0043OpenapiSlurmdbdJobsResp**](V0043OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Job description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_jobs**
> V0043OpenapiSlurmdbdJobsResp slurmdb_v0043_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_jobs_resp import V0043OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    scheduler_unset = 'scheduler_unset_example' # str | Schedule bits not set (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str | Job was started on submit (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str | Job was started from main scheduler (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str | Job was started from backfill (optional)
    job_started = 'job_started_example' # str | Job start RPC was received (optional)
    exit_code = 'exit_code_example' # str | Job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str | Include duplicate job entries (optional)
    skip_steps = 'skip_steps_example' # str | Exclude job step details (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str | Do not truncate the time to usage_start and usage_end (optional)
    whole_hetjob = 'whole_hetjob_example' # str | Include details on all hetjob components (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str | Only show details on specified hetjob components (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str | Tell dbd not to wait for the result (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str | Use usage_time as the submit_time of the job (optional)
    show_batch_script = 'show_batch_script_example' # str | Include job script (optional)
    show_job_environment = 'show_job_environment_example' # str | Include job environment (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    end_time = 'end_time_example' # str | Usage end (UNIX timestamp) (optional)
    start_time = 'start_time_example' # str | Usage start (UNIX timestamp) (optional)
    node = 'node_example' # str | Ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV WCKey list (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0043_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->slurmdb_v0043_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **scheduler_unset** | **str**| Schedule bits not set | [optional] 
 **scheduled_on_submit** | **str**| Job was started on submit | [optional] 
 **scheduled_by_main** | **str**| Job was started from main scheduler | [optional] 
 **scheduled_by_backfill** | **str**| Job was started from backfill | [optional] 
 **job_started** | **str**| Job start RPC was received | [optional] 
 **exit_code** | **str**| Job exit code (numeric) | [optional] 
 **show_duplicates** | **str**| Include duplicate job entries | [optional] 
 **skip_steps** | **str**| Exclude job step details | [optional] 
 **disable_truncate_usage_time** | **str**| Do not truncate the time to usage_start and usage_end | [optional] 
 **whole_hetjob** | **str**| Include details on all hetjob components | [optional] 
 **disable_whole_hetjob** | **str**| Only show details on specified hetjob components | [optional] 
 **disable_wait_for_result** | **str**| Tell dbd not to wait for the result | [optional] 
 **usage_time_as_submit_time** | **str**| Use usage_time as the submit_time of the job | [optional] 
 **show_batch_script** | **str**| Include job script | [optional] 
 **show_job_environment** | **str**| Include job environment | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **end_time** | **str**| Usage end (UNIX timestamp) | [optional] 
 **start_time** | **str**| Usage start (UNIX timestamp) | [optional] 
 **node** | **str**| Ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV WCKey list | [optional] 

### Return type

[**V0043OpenapiSlurmdbdJobsResp**](V0043OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | List of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_ping**
> V0043OpenapiSlurmdbdPingResp slurmdb_v0043_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_ping_resp import V0043OpenapiSlurmdbdPingResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurmdb_v0043_get_ping()
        print("The response of SlurmdbApi->slurmdb_v0043_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0043OpenapiSlurmdbdPingResp**](V0043OpenapiSlurmdbdPingResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_qos**
> V0043OpenapiSlurmdbdQosResp slurmdb_v0043_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_qos_resp import V0043OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0043_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)
        print("The response of SlurmdbApi->slurmdb_v0043_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 

### Return type

[**V0043OpenapiSlurmdbdQosResp**](V0043OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS |  -  |
**0** | List of QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_single_qos**
> V0043OpenapiSlurmdbdQosResp slurmdb_v0043_get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_slurmdbd_qos_resp import V0043OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0043_get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0043_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**V0043OpenapiSlurmdbdQosResp**](V0043OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_tres**
> V0043OpenapiTresResp slurmdb_v0043_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_tres_resp import V0043OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0043_get_tres()
        print("The response of SlurmdbApi->slurmdb_v0043_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0043OpenapiTresResp**](V0043OpenapiTresResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | List of TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_user**
> V0043OpenapiUsersResp slurmdb_v0043_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_users_resp import V0043OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include WCKeys (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0043_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->slurmdb_v0043_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include WCKeys | [optional] 

### Return type

[**V0043OpenapiUsersResp**](V0043OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_users**
> V0043OpenapiUsersResp slurmdb_v0043_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_users_resp import V0043OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default WCKey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With WCKeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0043_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->slurmdb_v0043_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default WCKey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With WCKeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**V0043OpenapiUsersResp**](V0043OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_wckey**
> V0043OpenapiWckeyResp slurmdb_v0043_get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_wckey_resp import V0043OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0043_get_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0043_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0043OpenapiWckeyResp**](V0043OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Description of wckey |  -  |
**0** | Description of wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_get_wckeys**
> V0043OpenapiWckeyResp slurmdb_v0043_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_wckey_resp import V0043OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0043_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0043_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 

### Return type

[**V0043OpenapiWckeyResp**](V0043OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | List of wckeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_accounts**
> V0043OpenapiResp slurmdb_v0043_post_accounts(v0043_openapi_accounts_resp=v0043_openapi_accounts_resp)

Add/update list of accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_accounts_resp import V0043OpenapiAccountsResp
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_accounts_resp = slurmrestapi.V0043OpenapiAccountsResp() # V0043OpenapiAccountsResp | Description of accounts to update/create (optional)

    try:
        # Add/update list of accounts
        api_response = api_instance.slurmdb_v0043_post_accounts(v0043_openapi_accounts_resp=v0043_openapi_accounts_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_accounts_resp** | [**V0043OpenapiAccountsResp**](V0043OpenapiAccountsResp.md)| Description of accounts to update/create | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account update request |  -  |
**0** | Status of account update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_accounts_association**
> V0043OpenapiAccountsAddCondRespStr slurmdb_v0043_post_accounts_association(v0043_openapi_accounts_add_cond_resp=v0043_openapi_accounts_add_cond_resp)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_accounts_add_cond_resp import V0043OpenapiAccountsAddCondResp
from slurmrestapi.models.v0043_openapi_accounts_add_cond_resp_str import V0043OpenapiAccountsAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_accounts_add_cond_resp = slurmrestapi.V0043OpenapiAccountsAddCondResp() # V0043OpenapiAccountsAddCondResp | Add list of accounts with conditional association (optional)

    try:
        # Add accounts with conditional association
        api_response = api_instance.slurmdb_v0043_post_accounts_association(v0043_openapi_accounts_add_cond_resp=v0043_openapi_accounts_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_accounts_add_cond_resp** | [**V0043OpenapiAccountsAddCondResp**](V0043OpenapiAccountsAddCondResp.md)| Add list of accounts with conditional association | [optional] 

### Return type

[**V0043OpenapiAccountsAddCondRespStr**](V0043OpenapiAccountsAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account addition request |  -  |
**0** | Status of account addition request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_associations**
> V0043OpenapiResp slurmdb_v0043_post_associations(v0043_openapi_assocs_resp=v0043_openapi_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_assocs_resp import V0043OpenapiAssocsResp
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_assocs_resp = slurmrestapi.V0043OpenapiAssocsResp() # V0043OpenapiAssocsResp | Job description (optional)

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0043_post_associations(v0043_openapi_assocs_resp=v0043_openapi_assocs_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_assocs_resp** | [**V0043OpenapiAssocsResp**](V0043OpenapiAssocsResp.md)| Job description | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | status of associations update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_clusters**
> V0043OpenapiResp slurmdb_v0043_post_clusters(update_time=update_time, v0043_openapi_clusters_resp=v0043_openapi_clusters_resp)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_clusters_resp import V0043OpenapiClustersResp
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)
    v0043_openapi_clusters_resp = slurmrestapi.V0043OpenapiClustersResp() # V0043OpenapiClustersResp | Cluster add or update descriptions (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0043_post_clusters(update_time=update_time, v0043_openapi_clusters_resp=v0043_openapi_clusters_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 
 **v0043_openapi_clusters_resp** | [**V0043OpenapiClustersResp**](V0043OpenapiClustersResp.md)| Cluster add or update descriptions | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of modify clusters request |  -  |
**0** | Result of modify clusters request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_config**
> V0043OpenapiResp slurmdb_v0043_post_config(v0043_openapi_slurmdbd_config_resp=v0043_openapi_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.models.v0043_openapi_slurmdbd_config_resp import V0043OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_slurmdbd_config_resp = slurmrestapi.V0043OpenapiSlurmdbdConfigResp() # V0043OpenapiSlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0043_post_config(v0043_openapi_slurmdbd_config_resp=v0043_openapi_slurmdbd_config_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_slurmdbd_config_resp** | [**V0043OpenapiSlurmdbdConfigResp**](V0043OpenapiSlurmdbdConfigResp.md)| Add or update config | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_qos**
> V0043OpenapiResp slurmdb_v0043_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0043_openapi_slurmdbd_qos_resp=v0043_openapi_slurmdbd_qos_resp)

Add or update QOSs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.models.v0043_openapi_slurmdbd_qos_resp import V0043OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    v0043_openapi_slurmdbd_qos_resp = slurmrestapi.V0043OpenapiSlurmdbdQosResp() # V0043OpenapiSlurmdbdQosResp | Description of QOS to add or update (optional)

    try:
        # Add or update QOSs
        api_response = api_instance.slurmdb_v0043_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0043_openapi_slurmdbd_qos_resp=v0043_openapi_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **v0043_openapi_slurmdbd_qos_resp** | [**V0043OpenapiSlurmdbdQosResp**](V0043OpenapiSlurmdbdQosResp.md)| Description of QOS to add or update | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | QOS update response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_tres**
> V0043OpenapiResp slurmdb_v0043_post_tres(v0043_openapi_tres_resp=v0043_openapi_tres_resp)

Add TRES

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.models.v0043_openapi_tres_resp import V0043OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_tres_resp = slurmrestapi.V0043OpenapiTresResp() # V0043OpenapiTresResp | TRES descriptions. Only works in developer mode. (optional)

    try:
        # Add TRES
        api_response = api_instance.slurmdb_v0043_post_tres(v0043_openapi_tres_resp=v0043_openapi_tres_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_tres_resp** | [**V0043OpenapiTresResp**](V0043OpenapiTresResp.md)| TRES descriptions. Only works in developer mode. | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TRES update result |  -  |
**0** | TRES update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_users**
> V0043OpenapiResp slurmdb_v0043_post_users(v0043_openapi_users_resp=v0043_openapi_users_resp)

Update users

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.models.v0043_openapi_users_resp import V0043OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0043_openapi_users_resp = slurmrestapi.V0043OpenapiUsersResp() # V0043OpenapiUsersResp | add or update user (optional)

    try:
        # Update users
        api_response = api_instance.slurmdb_v0043_post_users(v0043_openapi_users_resp=v0043_openapi_users_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0043_openapi_users_resp** | [**V0043OpenapiUsersResp**](V0043OpenapiUsersResp.md)| add or update user | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of user update request |  -  |
**0** | Status of user update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_users_association**
> V0043OpenapiUsersAddCondRespStr slurmdb_v0043_post_users_association(update_time=update_time, flags=flags, v0043_openapi_users_add_cond_resp=v0043_openapi_users_add_cond_resp)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_users_add_cond_resp import V0043OpenapiUsersAddCondResp
from slurmrestapi.models.v0043_openapi_users_add_cond_resp_str import V0043OpenapiUsersAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)
    v0043_openapi_users_add_cond_resp = slurmrestapi.V0043OpenapiUsersAddCondResp() # V0043OpenapiUsersAddCondResp | Create users with conditional association (optional)

    try:
        # Add users with conditional association
        api_response = api_instance.slurmdb_v0043_post_users_association(update_time=update_time, flags=flags, v0043_openapi_users_add_cond_resp=v0043_openapi_users_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **v0043_openapi_users_add_cond_resp** | [**V0043OpenapiUsersAddCondResp**](V0043OpenapiUsersAddCondResp.md)| Create users with conditional association | [optional] 

### Return type

[**V0043OpenapiUsersAddCondRespStr**](V0043OpenapiUsersAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Add list of users with conditional association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0043_post_wckeys**
> V0043OpenapiResp slurmdb_v0043_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0043_openapi_wckey_resp=v0043_openapi_wckey_resp)

Add or update wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0043_openapi_resp import V0043OpenapiResp
from slurmrestapi.models.v0043_openapi_wckey_resp import V0043OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)
    v0043_openapi_wckey_resp = slurmrestapi.V0043OpenapiWckeyResp() # V0043OpenapiWckeyResp | wckeys description (optional)

    try:
        # Add or update wckeys
        api_response = api_instance.slurmdb_v0043_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0043_openapi_wckey_resp=v0043_openapi_wckey_resp)
        print("The response of SlurmdbApi->slurmdb_v0043_post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0043_post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 
 **v0043_openapi_wckey_resp** | [**V0043OpenapiWckeyResp**](V0043OpenapiWckeyResp.md)| wckeys description | [optional] 

### Return type

[**V0043OpenapiResp**](V0043OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey addition or update request |  -  |
**0** | Result of wckey addition or update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_account**
> V0044OpenapiAccountsRemovedResp slurmdb_v0044_delete_account(account_name)

Delete account

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_accounts_removed_resp import V0044OpenapiAccountsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name

    try:
        # Delete account
        api_response = api_instance.slurmdb_v0044_delete_account(account_name)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 

### Return type

[**V0044OpenapiAccountsRemovedResp**](V0044OpenapiAccountsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account deletion request |  -  |
**0** | Status of account deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_association**
> V0044OpenapiAssocsRemovedResp slurmdb_v0044_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_assocs_removed_resp import V0044OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete association
        api_response = api_instance.slurmdb_v0044_delete_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0044OpenapiAssocsRemovedResp**](V0044OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of associations delete request |  -  |
**0** | Status of associations delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_associations**
> V0044OpenapiAssocsRemovedResp slurmdb_v0044_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Delete associations

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_assocs_removed_resp import V0044OpenapiAssocsRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Delete associations
        api_response = api_instance.slurmdb_v0044_delete_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0044OpenapiAssocsRemovedResp**](V0044OpenapiAssocsRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations deleted |  -  |
**0** | List of associations deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_cluster**
> V0044OpenapiClustersRemovedResp slurmdb_v0044_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Delete cluster

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_clusters_removed_resp import V0044OpenapiClustersRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Delete cluster
        api_response = api_instance.slurmdb_v0044_delete_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0044OpenapiClustersRemovedResp**](V0044OpenapiClustersRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of delete cluster request |  -  |
**0** | Result of delete cluster request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_single_qos**
> V0044OpenapiSlurmdbdQosRemovedResp slurmdb_v0044_delete_single_qos(qos)

Delete QOS

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_qos_removed_resp import V0044OpenapiSlurmdbdQosRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name

    try:
        # Delete QOS
        api_response = api_instance.slurmdb_v0044_delete_single_qos(qos)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 

### Return type

[**V0044OpenapiSlurmdbdQosRemovedResp**](V0044OpenapiSlurmdbdQosRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_user**
> V0044OpenapiResp slurmdb_v0044_delete_user(name)

Delete user

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name

    try:
        # Delete user
        api_response = api_instance.slurmdb_v0044_delete_user(name)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of user delete request |  -  |
**0** | Result of user delete request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_delete_wckey**
> V0044OpenapiWckeyRemovedResp slurmdb_v0044_delete_wckey(id)

Delete wckey

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_wckey_removed_resp import V0044OpenapiWckeyRemovedResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Delete wckey
        api_response = api_instance.slurmdb_v0044_delete_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0044_delete_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_delete_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0044OpenapiWckeyRemovedResp**](V0044OpenapiWckeyRemovedResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey deletion request |  -  |
**0** | Result of wckey deletion request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_account**
> V0044OpenapiAccountsResp slurmdb_v0044_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)

Get account info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_accounts_resp import V0044OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account_name = 'account_name_example' # str | Account name
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted (optional)

    try:
        # Get account info
        api_response = api_instance.slurmdb_v0044_get_account(account_name, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0044_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Account name | 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_deleted** | **str**| Include deleted | [optional] 

### Return type

[**V0044OpenapiAccountsResp**](V0044OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_accounts**
> V0044OpenapiAccountsResp slurmdb_v0044_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)

Get account list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_accounts_resp import V0044OpenapiAccountsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    deleted = 'deleted_example' # str | include deleted associations (optional)
    with_associations = 'with_associations_example' # str | query includes associations (optional)
    with_coordinators = 'with_coordinators_example' # str | query includes coordinators (optional)
    no_users_are_coords = 'no_users_are_coords_example' # str | remove users as coordinators (optional)
    users_are_coords = 'users_are_coords_example' # str | users are coordinators (optional)

    try:
        # Get account list
        api_response = api_instance.slurmdb_v0044_get_accounts(description=description, deleted=deleted, with_associations=with_associations, with_coordinators=with_coordinators, no_users_are_coords=no_users_are_coords, users_are_coords=users_are_coords)
        print("The response of SlurmdbApi->slurmdb_v0044_get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **deleted** | **str**| include deleted associations | [optional] 
 **with_associations** | **str**| query includes associations | [optional] 
 **with_coordinators** | **str**| query includes coordinators | [optional] 
 **no_users_are_coords** | **str**| remove users as coordinators | [optional] 
 **users_are_coords** | **str**| users are coordinators | [optional] 

### Return type

[**V0044OpenapiAccountsResp**](V0044OpenapiAccountsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of accounts |  -  |
**0** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_association**
> V0044OpenapiAssocsResp slurmdb_v0044_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_assocs_resp import V0044OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association info
        api_response = api_instance.slurmdb_v0044_get_association(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0044_get_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0044OpenapiAssocsResp**](V0044OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_associations**
> V0044OpenapiAssocsResp slurmdb_v0044_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)

Get association list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_assocs_resp import V0044OpenapiAssocsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV accounts list (optional)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    default_qos = 'default_qos_example' # str | CSV QOS list (optional)
    include_deleted_associations = 'include_deleted_associations_example' # str |  (optional)
    include_usage = 'include_usage_example' # str |  (optional)
    filter_to_only_defaults = 'filter_to_only_defaults_example' # str |  (optional)
    include_the_raw_qos_or_delta_qos = 'include_the_raw_qos_or_delta_qos_example' # str |  (optional)
    include_sub_acct_information = 'include_sub_acct_information_example' # str |  (optional)
    exclude_parent_id_name = 'exclude_parent_id_name_example' # str |  (optional)
    exclude_limits_from_parents = 'exclude_limits_from_parents_example' # str |  (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    parent_account = 'parent_account_example' # str | CSV names of parent account (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)

    try:
        # Get association list
        api_response = api_instance.slurmdb_v0044_get_associations(account=account, cluster=cluster, default_qos=default_qos, include_deleted_associations=include_deleted_associations, include_usage=include_usage, filter_to_only_defaults=filter_to_only_defaults, include_the_raw_qos_or_delta_qos=include_the_raw_qos_or_delta_qos, include_sub_acct_information=include_sub_acct_information, exclude_parent_id_name=exclude_parent_id_name, exclude_limits_from_parents=exclude_limits_from_parents, format=format, id=id, parent_account=parent_account, partition=partition, qos=qos, usage_end=usage_end, usage_start=usage_start, user=user)
        print("The response of SlurmdbApi->slurmdb_v0044_get_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV accounts list | [optional] 
 **cluster** | **str**| CSV clusters list | [optional] 
 **default_qos** | **str**| CSV QOS list | [optional] 
 **include_deleted_associations** | **str**|  | [optional] 
 **include_usage** | **str**|  | [optional] 
 **filter_to_only_defaults** | **str**|  | [optional] 
 **include_the_raw_qos_or_delta_qos** | **str**|  | [optional] 
 **include_sub_acct_information** | **str**|  | [optional] 
 **exclude_parent_id_name** | **str**|  | [optional] 
 **exclude_limits_from_parents** | **str**|  | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **parent_account** | **str**| CSV names of parent account | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 

### Return type

[**V0044OpenapiAssocsResp**](V0044OpenapiAssocsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of associations |  -  |
**0** | List of associations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_cluster**
> V0044OpenapiClustersResp slurmdb_v0044_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)

Get cluster info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_clusters_resp import V0044OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    classification = 'classification_example' # str | Type of machine (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    federation = 'federation_example' # str | CSV federation list (optional)
    flags = 'flags_example' # str | Query flags (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    rpc_version = 'rpc_version_example' # str | CSV RPC version list (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted clusters (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)

    try:
        # Get cluster info
        api_response = api_instance.slurmdb_v0044_get_cluster(cluster_name, classification=classification, cluster=cluster, federation=federation, flags=flags, format=format, rpc_version=rpc_version, usage_end=usage_end, usage_start=usage_start, with_deleted=with_deleted, with_usage=with_usage)
        print("The response of SlurmdbApi->slurmdb_v0044_get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **classification** | **str**| Type of machine | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **federation** | **str**| CSV federation list | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **rpc_version** | **str**| CSV RPC version list | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **with_deleted** | **str**| Include deleted clusters | [optional] 
 **with_usage** | **str**| Include usage | [optional] 

### Return type

[**V0044OpenapiClustersResp**](V0044OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster information |  -  |
**0** | Cluster information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_clusters**
> V0044OpenapiClustersResp slurmdb_v0044_get_clusters(update_time=update_time)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_clusters_resp import V0044OpenapiClustersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0044_get_clusters(update_time=update_time)
        print("The response of SlurmdbApi->slurmdb_v0044_get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 

### Return type

[**V0044OpenapiClustersResp**](V0044OpenapiClustersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters |  -  |
**0** | List of clusters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_config**
> V0044OpenapiSlurmdbdConfigResp slurmdb_v0044_get_config()

Dump all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_config_resp import V0044OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Dump all configuration information
        api_response = api_instance.slurmdb_v0044_get_config()
        print("The response of SlurmdbApi->slurmdb_v0044_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0044OpenapiSlurmdbdConfigResp**](V0044OpenapiSlurmdbdConfigResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_diag**
> V0044OpenapiSlurmdbdStatsResp slurmdb_v0044_get_diag()

Get slurmdb diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_stats_resp import V0044OpenapiSlurmdbdStatsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get slurmdb diagnostics
        api_response = api_instance.slurmdb_v0044_get_diag()
        print("The response of SlurmdbApi->slurmdb_v0044_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0044OpenapiSlurmdbdStatsResp**](V0044OpenapiSlurmdbdStatsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of statistics |  -  |
**0** | Dictionary of statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_instance**
> V0044OpenapiInstancesResp slurmdb_v0044_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_instances_resp import V0044OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance info
        api_response = api_instance.slurmdb_v0044_get_instance(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0044_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0044OpenapiInstancesResp**](V0044OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_instances**
> V0044OpenapiInstancesResp slurmdb_v0044_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)

Get instance list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_instances_resp import V0044OpenapiInstancesResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV clusters list (optional)
    extra = 'extra_example' # str | CSV extra list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    instance_id = 'instance_id_example' # str | CSV instance_id list (optional)
    instance_type = 'instance_type_example' # str | CSV instance_type list (optional)
    node_list = 'node_list_example' # str | Ranged node string (optional)
    time_end = 'time_end_example' # str | Time end (UNIX timestamp) (optional)
    time_start = 'time_start_example' # str | Time start (UNIX timestamp) (optional)

    try:
        # Get instance list
        api_response = api_instance.slurmdb_v0044_get_instances(cluster=cluster, extra=extra, format=format, instance_id=instance_id, instance_type=instance_type, node_list=node_list, time_end=time_end, time_start=time_start)
        print("The response of SlurmdbApi->slurmdb_v0044_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV clusters list | [optional] 
 **extra** | **str**| CSV extra list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **instance_id** | **str**| CSV instance_id list | [optional] 
 **instance_type** | **str**| CSV instance_type list | [optional] 
 **node_list** | **str**| Ranged node string | [optional] 
 **time_end** | **str**| Time end (UNIX timestamp) | [optional] 
 **time_start** | **str**| Time start (UNIX timestamp) | [optional] 

### Return type

[**V0044OpenapiInstancesResp**](V0044OpenapiInstancesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of instances |  -  |
**0** | List of instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_job**
> V0044OpenapiSlurmdbdJobsResp slurmdb_v0044_get_job(job_id)

Get job info

This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_jobs_resp import V0044OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get job info
        api_response = api_instance.slurmdb_v0044_get_job(job_id)
        print("The response of SlurmdbApi->slurmdb_v0044_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**V0044OpenapiSlurmdbdJobsResp**](V0044OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job description |  -  |
**0** | Job description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_jobs**
> V0044OpenapiSlurmdbdJobsResp slurmdb_v0044_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, job_altered=job_altered, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)

Get job list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_jobs_resp import V0044OpenapiSlurmdbdJobsResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    account = 'account_example' # str | CSV account list (optional)
    association = 'association_example' # str | CSV association list (optional)
    cluster = 'cluster_example' # str | CSV cluster list (optional)
    constraints = 'constraints_example' # str | CSV constraint list (optional)
    scheduler_unset = 'scheduler_unset_example' # str | Schedule bits not set (optional)
    scheduled_on_submit = 'scheduled_on_submit_example' # str | Job was started on submit (optional)
    scheduled_by_main = 'scheduled_by_main_example' # str | Job was started from main scheduler (optional)
    scheduled_by_backfill = 'scheduled_by_backfill_example' # str | Job was started from backfill (optional)
    job_started = 'job_started_example' # str | Job start RPC was received (optional)
    job_altered = 'job_altered_example' # str | Job record has been altered (optional)
    exit_code = 'exit_code_example' # str | Job exit code (numeric) (optional)
    show_duplicates = 'show_duplicates_example' # str | Include duplicate job entries (optional)
    skip_steps = 'skip_steps_example' # str | Exclude job step details (optional)
    disable_truncate_usage_time = 'disable_truncate_usage_time_example' # str | Do not truncate the time to usage_start and usage_end (optional)
    whole_hetjob = 'whole_hetjob_example' # str | Include details on all hetjob components (optional)
    disable_whole_hetjob = 'disable_whole_hetjob_example' # str | Only show details on specified hetjob components (optional)
    disable_wait_for_result = 'disable_wait_for_result_example' # str | Tell dbd not to wait for the result (optional)
    usage_time_as_submit_time = 'usage_time_as_submit_time_example' # str | Use usage_time as the submit_time of the job (optional)
    show_batch_script = 'show_batch_script_example' # str | Include job script (optional)
    show_job_environment = 'show_job_environment_example' # str | Include job environment (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    groups = 'groups_example' # str | CSV group list (optional)
    job_name = 'job_name_example' # str | CSV job name list (optional)
    partition = 'partition_example' # str | CSV partition name list (optional)
    qos = 'qos_example' # str | CSV QOS name list (optional)
    reason = 'reason_example' # str | CSV reason list (optional)
    reservation = 'reservation_example' # str | CSV reservation name list (optional)
    reservation_id = 'reservation_id_example' # str | CSV reservation ID list (optional)
    state = 'state_example' # str | CSV state list (optional)
    step = 'step_example' # str | CSV step id list (optional)
    end_time = 'end_time_example' # str | Usage end (UNIX timestamp) (optional)
    start_time = 'start_time_example' # str | Usage start (UNIX timestamp) (optional)
    node = 'node_example' # str | Ranged node string where jobs ran (optional)
    users = 'users_example' # str | CSV user name list (optional)
    wckey = 'wckey_example' # str | CSV WCKey list (optional)

    try:
        # Get job list
        api_response = api_instance.slurmdb_v0044_get_jobs(account=account, association=association, cluster=cluster, constraints=constraints, scheduler_unset=scheduler_unset, scheduled_on_submit=scheduled_on_submit, scheduled_by_main=scheduled_by_main, scheduled_by_backfill=scheduled_by_backfill, job_started=job_started, job_altered=job_altered, exit_code=exit_code, show_duplicates=show_duplicates, skip_steps=skip_steps, disable_truncate_usage_time=disable_truncate_usage_time, whole_hetjob=whole_hetjob, disable_whole_hetjob=disable_whole_hetjob, disable_wait_for_result=disable_wait_for_result, usage_time_as_submit_time=usage_time_as_submit_time, show_batch_script=show_batch_script, show_job_environment=show_job_environment, format=format, groups=groups, job_name=job_name, partition=partition, qos=qos, reason=reason, reservation=reservation, reservation_id=reservation_id, state=state, step=step, end_time=end_time, start_time=start_time, node=node, users=users, wckey=wckey)
        print("The response of SlurmdbApi->slurmdb_v0044_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| CSV account list | [optional] 
 **association** | **str**| CSV association list | [optional] 
 **cluster** | **str**| CSV cluster list | [optional] 
 **constraints** | **str**| CSV constraint list | [optional] 
 **scheduler_unset** | **str**| Schedule bits not set | [optional] 
 **scheduled_on_submit** | **str**| Job was started on submit | [optional] 
 **scheduled_by_main** | **str**| Job was started from main scheduler | [optional] 
 **scheduled_by_backfill** | **str**| Job was started from backfill | [optional] 
 **job_started** | **str**| Job start RPC was received | [optional] 
 **job_altered** | **str**| Job record has been altered | [optional] 
 **exit_code** | **str**| Job exit code (numeric) | [optional] 
 **show_duplicates** | **str**| Include duplicate job entries | [optional] 
 **skip_steps** | **str**| Exclude job step details | [optional] 
 **disable_truncate_usage_time** | **str**| Do not truncate the time to usage_start and usage_end | [optional] 
 **whole_hetjob** | **str**| Include details on all hetjob components | [optional] 
 **disable_whole_hetjob** | **str**| Only show details on specified hetjob components | [optional] 
 **disable_wait_for_result** | **str**| Tell dbd not to wait for the result | [optional] 
 **usage_time_as_submit_time** | **str**| Use usage_time as the submit_time of the job | [optional] 
 **show_batch_script** | **str**| Include job script | [optional] 
 **show_job_environment** | **str**| Include job environment | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **groups** | **str**| CSV group list | [optional] 
 **job_name** | **str**| CSV job name list | [optional] 
 **partition** | **str**| CSV partition name list | [optional] 
 **qos** | **str**| CSV QOS name list | [optional] 
 **reason** | **str**| CSV reason list | [optional] 
 **reservation** | **str**| CSV reservation name list | [optional] 
 **reservation_id** | **str**| CSV reservation ID list | [optional] 
 **state** | **str**| CSV state list | [optional] 
 **step** | **str**| CSV step id list | [optional] 
 **end_time** | **str**| Usage end (UNIX timestamp) | [optional] 
 **start_time** | **str**| Usage start (UNIX timestamp) | [optional] 
 **node** | **str**| Ranged node string where jobs ran | [optional] 
 **users** | **str**| CSV user name list | [optional] 
 **wckey** | **str**| CSV WCKey list | [optional] 

### Return type

[**V0044OpenapiSlurmdbdJobsResp**](V0044OpenapiSlurmdbdJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**0** | List of jobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_ping**
> V0044OpenapiSlurmdbdPingResp slurmdb_v0044_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_ping_resp import V0044OpenapiSlurmdbdPingResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurmdb_v0044_get_ping()
        print("The response of SlurmdbApi->slurmdb_v0044_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0044OpenapiSlurmdbdPingResp**](V0044OpenapiSlurmdbdPingResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_qos**
> V0044OpenapiSlurmdbdQosResp slurmdb_v0044_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)

Get QOS list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_qos_resp import V0044OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)

    try:
        # Get QOS list
        api_response = api_instance.slurmdb_v0044_get_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode)
        print("The response of SlurmdbApi->slurmdb_v0044_get_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 

### Return type

[**V0044OpenapiSlurmdbdQosResp**](V0044OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QOS |  -  |
**0** | List of QOS |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_single_qos**
> V0044OpenapiSlurmdbdQosResp slurmdb_v0044_get_single_qos(qos, with_deleted=with_deleted)

Get QOS info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_slurmdbd_qos_resp import V0044OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    qos = 'qos_example' # str | QOS name
    with_deleted = 'with_deleted_example' # str | Query includes deleted QOS (optional)

    try:
        # Get QOS info
        api_response = api_instance.slurmdb_v0044_get_single_qos(qos, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0044_get_single_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_single_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qos** | **str**| QOS name | 
 **with_deleted** | **str**| Query includes deleted QOS | [optional] 

### Return type

[**V0044OpenapiSlurmdbdQosResp**](V0044OpenapiSlurmdbdQosResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS information |  -  |
**0** | QOS information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_tres**
> V0044OpenapiTresResp slurmdb_v0044_get_tres()

Get TRES info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_tres_resp import V0044OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)

    try:
        # Get TRES info
        api_response = api_instance.slurmdb_v0044_get_tres()
        print("The response of SlurmdbApi->slurmdb_v0044_get_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_tres: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0044OpenapiTresResp**](V0044OpenapiTresResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TRES |  -  |
**0** | List of TRES |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_user**
> V0044OpenapiUsersResp slurmdb_v0044_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)

Get user info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_users_resp import V0044OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    name = 'name_example' # str | User name
    with_deleted = 'with_deleted_example' # str | Include deleted users (optional)
    with_assocs = 'with_assocs_example' # str | Include associations (optional)
    with_coords = 'with_coords_example' # str | Include coordinators (optional)
    with_wckeys = 'with_wckeys_example' # str | Include WCKeys (optional)

    try:
        # Get user info
        api_response = api_instance.slurmdb_v0044_get_user(name, with_deleted=with_deleted, with_assocs=with_assocs, with_coords=with_coords, with_wckeys=with_wckeys)
        print("The response of SlurmdbApi->slurmdb_v0044_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User name | 
 **with_deleted** | **str**| Include deleted users | [optional] 
 **with_assocs** | **str**| Include associations | [optional] 
 **with_coords** | **str**| Include coordinators | [optional] 
 **with_wckeys** | **str**| Include WCKeys | [optional] 

### Return type

[**V0044OpenapiUsersResp**](V0044OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_users**
> V0044OpenapiUsersResp slurmdb_v0044_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)

Get user list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_users_resp import V0044OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    admin_level = 'admin_level_example' # str | Administrator level (optional)
    default_account = 'default_account_example' # str | CSV default account list (optional)
    default_wckey = 'default_wckey_example' # str | CSV default WCKey list (optional)
    with_assocs = 'with_assocs_example' # str | With associations (optional)
    with_coords = 'with_coords_example' # str | With coordinators (optional)
    with_deleted = 'with_deleted_example' # str | With deleted (optional)
    with_wckeys = 'with_wckeys_example' # str | With WCKeys (optional)
    without_defaults = 'without_defaults_example' # str | Exclude defaults (optional)

    try:
        # Get user list
        api_response = api_instance.slurmdb_v0044_get_users(admin_level=admin_level, default_account=default_account, default_wckey=default_wckey, with_assocs=with_assocs, with_coords=with_coords, with_deleted=with_deleted, with_wckeys=with_wckeys, without_defaults=without_defaults)
        print("The response of SlurmdbApi->slurmdb_v0044_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_level** | **str**| Administrator level | [optional] 
 **default_account** | **str**| CSV default account list | [optional] 
 **default_wckey** | **str**| CSV default WCKey list | [optional] 
 **with_assocs** | **str**| With associations | [optional] 
 **with_coords** | **str**| With coordinators | [optional] 
 **with_deleted** | **str**| With deleted | [optional] 
 **with_wckeys** | **str**| With WCKeys | [optional] 
 **without_defaults** | **str**| Exclude defaults | [optional] 

### Return type

[**V0044OpenapiUsersResp**](V0044OpenapiUsersResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**0** | List of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_wckey**
> V0044OpenapiWckeyResp slurmdb_v0044_get_wckey(id)

Get wckey info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_wckey_resp import V0044OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    id = 'id_example' # str | WCKey ID

    try:
        # Get wckey info
        api_response = api_instance.slurmdb_v0044_get_wckey(id)
        print("The response of SlurmdbApi->slurmdb_v0044_get_wckey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_wckey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WCKey ID | 

### Return type

[**V0044OpenapiWckeyResp**](V0044OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Description of wckey |  -  |
**0** | Description of wckey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_get_wckeys**
> V0044OpenapiWckeyResp slurmdb_v0044_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)

Get wckey list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_wckey_resp import V0044OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)

    try:
        # Get wckey list
        api_response = api_instance.slurmdb_v0044_get_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted)
        print("The response of SlurmdbApi->slurmdb_v0044_get_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_get_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 

### Return type

[**V0044OpenapiWckeyResp**](V0044OpenapiWckeyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wckeys |  -  |
**0** | List of wckeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_accounts**
> V0044OpenapiResp slurmdb_v0044_post_accounts(v0044_openapi_accounts_resp=v0044_openapi_accounts_resp)

Add/update list of accounts

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_accounts_resp import V0044OpenapiAccountsResp
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_accounts_resp = slurmrestapi.V0044OpenapiAccountsResp() # V0044OpenapiAccountsResp | Description of accounts to update/create (optional)

    try:
        # Add/update list of accounts
        api_response = api_instance.slurmdb_v0044_post_accounts(v0044_openapi_accounts_resp=v0044_openapi_accounts_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_accounts_resp** | [**V0044OpenapiAccountsResp**](V0044OpenapiAccountsResp.md)| Description of accounts to update/create | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account update request |  -  |
**0** | Status of account update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_accounts_association**
> V0044OpenapiAccountsAddCondRespStr slurmdb_v0044_post_accounts_association(v0044_openapi_accounts_add_cond_resp=v0044_openapi_accounts_add_cond_resp)

Add accounts with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_accounts_add_cond_resp import V0044OpenapiAccountsAddCondResp
from slurmrestapi.models.v0044_openapi_accounts_add_cond_resp_str import V0044OpenapiAccountsAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_accounts_add_cond_resp = slurmrestapi.V0044OpenapiAccountsAddCondResp() # V0044OpenapiAccountsAddCondResp | Add list of accounts with conditional association (optional)

    try:
        # Add accounts with conditional association
        api_response = api_instance.slurmdb_v0044_post_accounts_association(v0044_openapi_accounts_add_cond_resp=v0044_openapi_accounts_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_accounts_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_accounts_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_accounts_add_cond_resp** | [**V0044OpenapiAccountsAddCondResp**](V0044OpenapiAccountsAddCondResp.md)| Add list of accounts with conditional association | [optional] 

### Return type

[**V0044OpenapiAccountsAddCondRespStr**](V0044OpenapiAccountsAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of account addition request |  -  |
**0** | Status of account addition request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_associations**
> V0044OpenapiResp slurmdb_v0044_post_associations(v0044_openapi_assocs_resp=v0044_openapi_assocs_resp)

Set associations info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_assocs_resp import V0044OpenapiAssocsResp
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_assocs_resp = slurmrestapi.V0044OpenapiAssocsResp() # V0044OpenapiAssocsResp | Job description (optional)

    try:
        # Set associations info
        api_response = api_instance.slurmdb_v0044_post_associations(v0044_openapi_assocs_resp=v0044_openapi_assocs_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_assocs_resp** | [**V0044OpenapiAssocsResp**](V0044OpenapiAssocsResp.md)| Job description | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | status of associations update |  -  |
**0** | status of associations update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_clusters**
> V0044OpenapiResp slurmdb_v0044_post_clusters(update_time=update_time, v0044_openapi_clusters_resp=v0044_openapi_clusters_resp)

Get cluster list

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_clusters_resp import V0044OpenapiClustersResp
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query reservations updated more recently than this time (UNIX timestamp) (optional)
    v0044_openapi_clusters_resp = slurmrestapi.V0044OpenapiClustersResp() # V0044OpenapiClustersResp | Cluster add or update descriptions (optional)

    try:
        # Get cluster list
        api_response = api_instance.slurmdb_v0044_post_clusters(update_time=update_time, v0044_openapi_clusters_resp=v0044_openapi_clusters_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query reservations updated more recently than this time (UNIX timestamp) | [optional] 
 **v0044_openapi_clusters_resp** | [**V0044OpenapiClustersResp**](V0044OpenapiClustersResp.md)| Cluster add or update descriptions | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of modify clusters request |  -  |
**0** | Result of modify clusters request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_config**
> V0044OpenapiResp slurmdb_v0044_post_config(v0044_openapi_slurmdbd_config_resp=v0044_openapi_slurmdbd_config_resp)

Load all configuration information

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.models.v0044_openapi_slurmdbd_config_resp import V0044OpenapiSlurmdbdConfigResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_slurmdbd_config_resp = slurmrestapi.V0044OpenapiSlurmdbdConfigResp() # V0044OpenapiSlurmdbdConfigResp | Add or update config (optional)

    try:
        # Load all configuration information
        api_response = api_instance.slurmdb_v0044_post_config(v0044_openapi_slurmdbd_config_resp=v0044_openapi_slurmdbd_config_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_slurmdbd_config_resp** | [**V0044OpenapiSlurmdbdConfigResp**](V0044OpenapiSlurmdbdConfigResp.md)| Add or update config | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | slurmdbd configuration |  -  |
**0** | slurmdbd configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_job**
> V0044OpenapiJobModifyResp slurmdb_v0044_post_job(job_id, v0044_job_modify=v0044_job_modify)

Update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_job_modify import V0044JobModify
from slurmrestapi.models.v0044_openapi_job_modify_resp import V0044OpenapiJobModifyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    v0044_job_modify = slurmrestapi.V0044JobModify() # V0044JobModify | Job update description (optional)

    try:
        # Update job
        api_response = api_instance.slurmdb_v0044_post_job(job_id, v0044_job_modify=v0044_job_modify)
        print("The response of SlurmdbApi->slurmdb_v0044_post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **v0044_job_modify** | [**V0044JobModify**](V0044JobModify.md)| Job update description | [optional] 

### Return type

[**V0044OpenapiJobModifyResp**](V0044OpenapiJobModifyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job update results |  -  |
**0** | Job update results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_jobs**
> V0044OpenapiJobModifyResp slurmdb_v0044_post_jobs(v0044_openapi_job_modify_req=v0044_openapi_job_modify_req)

Update jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_job_modify_req import V0044OpenapiJobModifyReq
from slurmrestapi.models.v0044_openapi_job_modify_resp import V0044OpenapiJobModifyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_job_modify_req = slurmrestapi.V0044OpenapiJobModifyReq() # V0044OpenapiJobModifyReq | Job update description (optional)

    try:
        # Update jobs
        api_response = api_instance.slurmdb_v0044_post_jobs(v0044_openapi_job_modify_req=v0044_openapi_job_modify_req)
        print("The response of SlurmdbApi->slurmdb_v0044_post_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_job_modify_req** | [**V0044OpenapiJobModifyReq**](V0044OpenapiJobModifyReq.md)| Job update description | [optional] 

### Return type

[**V0044OpenapiJobModifyResp**](V0044OpenapiJobModifyResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job update results |  -  |
**0** | Job update results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_qos**
> V0044OpenapiResp slurmdb_v0044_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0044_openapi_slurmdbd_qos_resp=v0044_openapi_slurmdbd_qos_resp)

Add or update QOSs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.models.v0044_openapi_slurmdbd_qos_resp import V0044OpenapiSlurmdbdQosResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    description = 'description_example' # str | CSV description list (optional)
    include_deleted_qos = 'include_deleted_qos_example' # str |  (optional)
    id = 'id_example' # str | CSV QOS id list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    name = 'name_example' # str | CSV QOS name list (optional)
    preempt_mode = 'preempt_mode_example' # str | PreemptMode used when jobs in this QOS are preempted (optional)
    v0044_openapi_slurmdbd_qos_resp = slurmrestapi.V0044OpenapiSlurmdbdQosResp() # V0044OpenapiSlurmdbdQosResp | Description of QOS to add or update (optional)

    try:
        # Add or update QOSs
        api_response = api_instance.slurmdb_v0044_post_qos(description=description, include_deleted_qos=include_deleted_qos, id=id, format=format, name=name, preempt_mode=preempt_mode, v0044_openapi_slurmdbd_qos_resp=v0044_openapi_slurmdbd_qos_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_qos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_qos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| CSV description list | [optional] 
 **include_deleted_qos** | **str**|  | [optional] 
 **id** | **str**| CSV QOS id list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **name** | **str**| CSV QOS name list | [optional] 
 **preempt_mode** | **str**| PreemptMode used when jobs in this QOS are preempted | [optional] 
 **v0044_openapi_slurmdbd_qos_resp** | [**V0044OpenapiSlurmdbdQosResp**](V0044OpenapiSlurmdbdQosResp.md)| Description of QOS to add or update | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QOS update response |  -  |
**0** | QOS update response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_tres**
> V0044OpenapiResp slurmdb_v0044_post_tres(v0044_openapi_tres_resp=v0044_openapi_tres_resp)

Add TRES

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.models.v0044_openapi_tres_resp import V0044OpenapiTresResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_tres_resp = slurmrestapi.V0044OpenapiTresResp() # V0044OpenapiTresResp | TRES descriptions. Only works in developer mode. (optional)

    try:
        # Add TRES
        api_response = api_instance.slurmdb_v0044_post_tres(v0044_openapi_tres_resp=v0044_openapi_tres_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_tres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_tres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_tres_resp** | [**V0044OpenapiTresResp**](V0044OpenapiTresResp.md)| TRES descriptions. Only works in developer mode. | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TRES update result |  -  |
**0** | TRES update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_users**
> V0044OpenapiResp slurmdb_v0044_post_users(v0044_openapi_users_resp=v0044_openapi_users_resp)

Update users

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.models.v0044_openapi_users_resp import V0044OpenapiUsersResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    v0044_openapi_users_resp = slurmrestapi.V0044OpenapiUsersResp() # V0044OpenapiUsersResp | add or update user (optional)

    try:
        # Update users
        api_response = api_instance.slurmdb_v0044_post_users(v0044_openapi_users_resp=v0044_openapi_users_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0044_openapi_users_resp** | [**V0044OpenapiUsersResp**](V0044OpenapiUsersResp.md)| add or update user | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of user update request |  -  |
**0** | Status of user update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_users_association**
> V0044OpenapiUsersAddCondRespStr slurmdb_v0044_post_users_association(update_time=update_time, flags=flags, v0044_openapi_users_add_cond_resp=v0044_openapi_users_add_cond_resp)

Add users with conditional association

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_users_add_cond_resp import V0044OpenapiUsersAddCondResp
from slurmrestapi.models.v0044_openapi_users_add_cond_resp_str import V0044OpenapiUsersAddCondRespStr
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    update_time = 'update_time_example' # str | Query partitions updated more recently than this time (UNIX timestamp) (optional)
    flags = 'flags_example' # str | Query flags (optional)
    v0044_openapi_users_add_cond_resp = slurmrestapi.V0044OpenapiUsersAddCondResp() # V0044OpenapiUsersAddCondResp | Create users with conditional association (optional)

    try:
        # Add users with conditional association
        api_response = api_instance.slurmdb_v0044_post_users_association(update_time=update_time, flags=flags, v0044_openapi_users_add_cond_resp=v0044_openapi_users_add_cond_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_users_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_users_association: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Query partitions updated more recently than this time (UNIX timestamp) | [optional] 
 **flags** | **str**| Query flags | [optional] 
 **v0044_openapi_users_add_cond_resp** | [**V0044OpenapiUsersAddCondResp**](V0044OpenapiUsersAddCondResp.md)| Create users with conditional association | [optional] 

### Return type

[**V0044OpenapiUsersAddCondRespStr**](V0044OpenapiUsersAddCondRespStr.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add list of users with conditional association |  -  |
**0** | Add list of users with conditional association |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurmdb_v0044_post_wckeys**
> V0044OpenapiResp slurmdb_v0044_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0044_openapi_wckey_resp=v0044_openapi_wckey_resp)

Add or update wckeys

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrestapi
from slurmrestapi.models.v0044_openapi_resp import V0044OpenapiResp
from slurmrestapi.models.v0044_openapi_wckey_resp import V0044OpenapiWckeyResp
from slurmrestapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrestapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrestapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrestapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrestapi.SlurmdbApi(api_client)
    cluster = 'cluster_example' # str | CSV cluster name list (optional)
    format = 'format_example' # str | Ignored; process JSON manually to control output format (optional)
    id = 'id_example' # str | CSV ID list (optional)
    name = 'name_example' # str | CSV name list (optional)
    only_defaults = 'only_defaults_example' # str | Only query defaults (optional)
    usage_end = 'usage_end_example' # str | Usage end (UNIX timestamp) (optional)
    usage_start = 'usage_start_example' # str | Usage start (UNIX timestamp) (optional)
    user = 'user_example' # str | CSV user list (optional)
    with_usage = 'with_usage_example' # str | Include usage (optional)
    with_deleted = 'with_deleted_example' # str | Include deleted WCKeys (optional)
    v0044_openapi_wckey_resp = slurmrestapi.V0044OpenapiWckeyResp() # V0044OpenapiWckeyResp | wckeys description (optional)

    try:
        # Add or update wckeys
        api_response = api_instance.slurmdb_v0044_post_wckeys(cluster=cluster, format=format, id=id, name=name, only_defaults=only_defaults, usage_end=usage_end, usage_start=usage_start, user=user, with_usage=with_usage, with_deleted=with_deleted, v0044_openapi_wckey_resp=v0044_openapi_wckey_resp)
        print("The response of SlurmdbApi->slurmdb_v0044_post_wckeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmdbApi->slurmdb_v0044_post_wckeys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| CSV cluster name list | [optional] 
 **format** | **str**| Ignored; process JSON manually to control output format | [optional] 
 **id** | **str**| CSV ID list | [optional] 
 **name** | **str**| CSV name list | [optional] 
 **only_defaults** | **str**| Only query defaults | [optional] 
 **usage_end** | **str**| Usage end (UNIX timestamp) | [optional] 
 **usage_start** | **str**| Usage start (UNIX timestamp) | [optional] 
 **user** | **str**| CSV user list | [optional] 
 **with_usage** | **str**| Include usage | [optional] 
 **with_deleted** | **str**| Include deleted WCKeys | [optional] 
 **v0044_openapi_wckey_resp** | [**V0044OpenapiWckeyResp**](V0044OpenapiWckeyResp.md)| wckeys description | [optional] 

### Return type

[**V0044OpenapiResp**](V0044OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of wckey addition or update request |  -  |
**0** | Result of wckey addition or update request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

