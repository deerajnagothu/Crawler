$executingScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$scriptPath1 = Join-Path $executingScriptDirectory "VM_constants.ps1"
. $scriptPath1

function Yo
{
    param([string]$message)
    Write-Host -ForegroundColor DarkGray "$message"
}

function Wait-A-Min{
    param([int]$Time=1)

    if($Time -ge 1){
            ForEach ( $m in 1..$Time){
                $remaining=$Time-$m+1
                ForEach ($q in 1..30){
                    Write-Host -NoNewline -ForegroundColor DarkGray "_"
                }
                Yo "waiting ... $remaining min"
                ForEach ($q in 1..30){
                    sleep 2
                    Write-Host -NoNewline -BackgroundColor DarkGray "*"
                }
                Yo ""
            }
            Yo ""
    }
}
function GetStudentVMName
{
    param([string]$OriginVM,
            [int]$index)
    $result=$OriginVM+"_"+$StudentVAppPostfix+"_"+$index
    $result
}
#########################



#######################


$source_vapp = Get-VApp -Name $SourceVappName -ErrorAction Stop
Yo "Source VApp: $source_vapp"

#Create destination container vapp. This vapp will contain all student vapps.
Yo "Create or find container VApp to put all the lab in: $ContainerVAppName" 

$container_vapp=Get-VApp -Name $ContainerVAppName -ErrorAction SilentlyContinue
if (!$container_vapp){
    Yo "`t$ContainerVAppName doesn't exist. Creating ..." 
    $container_vapp=New-VApp -Name $ContainerVAppName -Location $vmhosts -ErrorAction Stop

}
else{
    Yo "`tFound existing container vapp $container_vapp" 
}

Yo "Perform VApp cloning $source_vapp to container $container_vapp"

$indicies = $start..$end
ForEach ( $index in $indicies) 
   { 
    
    Get-VM -Location $source_vapp | foreach {
        $srcVM=$_
        $dstVMName=(GetStudentVMName -OriginVM $srcVM -index $index)
        Yo "`t`tCloning $srcVM to $dstVMName on $vmhosts"    
                       
        $vm_object= New-VM -Name $dstVMName -VM $srcVM -VMHost $vmhosts -ResourcePool $container_vapp -Datastore $datastore_major -LinkedClone -ReferenceSnapshot $ReferenceSnapshotName  -RunAsync        
    }
}
Wait-A-Min -Time 1
exit
Start-VApp -VApp $ContainerVAppName

exit
