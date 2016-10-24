$start = 1
$end = 4

$SourceVappName = "Parent_Crawler"
$ContainerVAppName = "Mini_Crawlers"

$DatacenetrName = "CNS_DC"

$datastore_minor = "Datastore_58"
$datastore_major = "Datastore_58_part2"

$CrawlerVAppPrefix = "Crawler_"
$ReferenceSnapshotName = "Point_zero"

$datacenter=Get-Datacenter $DatacenetrName
Write-Host "Datacenter: $datacenter"

$vmhosts = Get-VMHost -Name "192.168.100.58"
Write-Host "Available VMHosts $vmhosts"

$datastores=Get-Datastore -Name $datastore_major
Write-Host "Datastores: $datastores" 