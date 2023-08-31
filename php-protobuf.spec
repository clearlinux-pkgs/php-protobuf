#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
#
Name     : php-protobuf
Version  : 3.24.1
Release  : 97
URL      : https://pecl.php.net/get/protobuf-3.24.1.tgz
Source0  : https://pecl.php.net/get/protobuf-3.24.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: php-protobuf-lib = %{version}-%{release}
Requires: php-protobuf-license = %{version}-%{release}
BuildRequires : buildreq-php
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the php-protobuf package.
Group: Libraries
Requires: php-protobuf-license = %{version}-%{release}

%description lib
lib components for the php-protobuf package.


%package license
Summary: license components for the php-protobuf package.
Group: Default

%description license
license components for the php-protobuf package.


%prep
%setup -q -n protobuf-3.24.1
cd %{_builddir}/protobuf-3.24.1
pushd ..
cp -a protobuf-3.24.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-protobuf
cp %{_builddir}/protobuf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6 || :
cp %{_builddir}/protobuf-%{version}/third_party/utf8_range/LICENSE %{buildroot}/usr/share/package-licenses/php-protobuf/252c7fd154ca740ae6f765d206fbd9119108a0e3 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/protobuf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/php-protobuf/252c7fd154ca740ae6f765d206fbd9119108a0e3
