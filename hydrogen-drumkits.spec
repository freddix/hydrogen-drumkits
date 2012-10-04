Summary:	Hydrogen drumkits
Name:		hydrogen-drumkits
Version:	1.0
Release:	14
License:	GPL and other
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/hydrogen/3355606kit.h2drumkit
# Source0-md5:	5dad41a4f0fb5a9fda0af98b9f553060
Source1:	http://downloads.sourceforge.net/hydrogen/Boss_DR-110.h2drumkit
# Source1-md5:	fb8ca90e4aa054a24fb07aa768b54d18
Source2:	http://downloads.sourceforge.net/hydrogen/Classic-626.h2drumkit
# Source2-md5:	86dbdb8d2f9b12690e92211d36c6fe7d
Source3:	http://downloads.sourceforge.net/hydrogen/Classic-808.h2drumkit
# Source3-md5:	c08d5093fc28a30a7542f0c89493e807
Source4:	http://downloads.sourceforge.net/hydrogen/ColomboAcousticDrumkit.h2drumkit
# Source4-md5:	cb11827e185ab5a6906967901495884b
Source5:	http://downloads.sourceforge.net/hydrogen/deathmetal-drumkit.h2drumkit
# Source5-md5:	0465025dcf6659657b773874d168c27b
Source6:	http://downloads.sourceforge.net/hydrogen/EasternHop-1.h2drumkit
# Source6-md5:	8750fcbe186e49a89bc18a9237ee6604
Source7:	http://downloads.sourceforge.net/hydrogen/ElectricEmpireKit.h2drumkit
# Source7-md5:	df1bd778148cc25d8f63a8cc7aa91fcb
Source8:	http://downloads.sourceforge.net/hydrogen/ErnysPercussion.h2drumkit
# Source8-md5:	0e96f5971d5db887a186d5739c12ab77
Source9:	http://downloads.sourceforge.net/hydrogen/HardElectro1.h2drumkit
# Source9-md5:	f953edf3f4227d786df59b544370e379
Source10:	http://downloads.sourceforge.net/hydrogen/HipHop-1.h2drumkit
# Source10-md5:	7f52d6ac56a31f5b618657d40d4eb86e
Source11:	http://downloads.sourceforge.net/hydrogen/HipHop-2.h2drumkit
# Source11-md5:	217f38ebf2849b20ff3a5dca1994be08
Source12:	http://downloads.sourceforge.net/hydrogen/K-27_Trash_Kit.h2drumkit
# Source12-md5:	f445c60d4625a6bfe6bb9dbac1ac0aa7
Source13:	http://downloads.sourceforge.net/hydrogen/Millo-Drums_v.1.h2drumkit
# Source13-md5:	4c895d59c3bc5f3322d14789de345be2
Source14:	http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered2.h2drumkit
# Source14-md5:	2da5b8ee87bce3e67464c61ba0b722dd
Source15:	http://downloads.sourceforge.net/hydrogen/Millo_MultiLayered3.h2drumkit
# Source15-md5:	79ca7360784ec72959aa07c3c584d76c
Source16:	http://downloads.sourceforge.net/hydrogen/Synthie-1.h2drumkit
# Source16-md5:	33f02627ac1489e4ab52c5f078c538b9
Source17:	http://downloads.sourceforge.net/hydrogen/TD-7kit.h2drumkit
# Source17-md5:	635274624e0a739c51b70f72a58cfcec
Source18:	http://downloads.sourceforge.net/hydrogen/Techno-1.h2drumkit
# Source18-md5:	f91912fc88361dd8954c11f2e602aa25
Source19:	http://downloads.sourceforge.net/hydrogen/TR808909.h2drumkit
# Source19-md5:	1db9cce82fbdaebac1ab4608be5853ea
Source20:	http://downloads.sourceforge.net/hydrogen/VariBreaks.h2drumkit
# Source20-md5:	a9c305829cd23c28ffd1647cb5c0bdfd
Source21:	http://downloads.sourceforge.net/hydrogen/YamahaVintageKit.h2drumkit
# Source21-md5:	8f63997dd789179fa009f84cc515fb3e
Source22:	http://downloads.sourceforge.net/hydrogen/UltraAcousticKit.tar.gz
# Source22-md5:	ee0974b404d34a2c5cf3d8f3952a80e9
# 3rd Party
Source30:	http://www.zetacentauri.com/software/KawaiXD-5Kit.h2drumkit
# Source30-md5:	ae974ec4550b64654cfb1fe42fe110af
Source31:	http://www.zetacentauri.com/software/RolandJD-990Kit.h2drumkit
# Source31-md5:	ef5ecfdea55835789c143c0bc3ac15e9
Source32:	http://www.zetacentauri.com/software/YamahaTG-55Kit.h2drumkit
# Source32-md5:	cf95db46c05287aaa1a18dff0b0ce335
Source33:	http://www.cluebyfour.org/%7Estreiner/PremierKit/PremierKit.tar.bz2
# Source33-md5:	350e45e3ec53ca4d40fd9a809af34f1c
Source40:	http://www.autodafe.net/downloads/GSCW-1.zip
# Source40-md5:	c7806c41b6b0bb5f2b355475f1be9dad
Source41:	http://www.autodafe.net/downloads/GSCW-2.zip
# Source41-md5:	1ce80cd9c7b7ebd909caccea01a46039
#
URL:		http://hydrogen.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	hydrogen

%define		hydrogendir	%{_datadir}/hydrogen/data

%description
Hydrogen drumkits.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a17 -a18 -a19 -a20 -a21 -a22 -a30 -a31 -a32 -a33 -a34 -a40 -a41

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{hydrogendir}/drumkits

tar zxf UltraAcousticKit/UltraAcousticKit.h2drumkit -C \
	$RPM_BUILD_ROOT%{hydrogendir}/drumkits

tar zxf GSCW-1.h2drumkit -C \
	$RPM_BUILD_ROOT%{hydrogendir}/drumkits
tar zxf GSCW-2.h2drumkit -C \
	$RPM_BUILD_ROOT%{hydrogendir}/drumkits
rm -f GSCW-*

cp -ar . $RPM_BUILD_ROOT%{hydrogendir}/drumkits
rm -f $RPM_BUILD_ROOT%{hydrogendir}/drumkits/*/*.{h2drumkit,h2song}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{hydrogendir}/drumkits

