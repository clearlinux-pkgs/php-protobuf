#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-protobuf
Version  : 3.21.4
Release  : 54
URL      : https://pecl.php.net/get/protobuf-3.21.4.tgz
Source0  : https://pecl.php.net/get/protobuf-3.21.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: php-protobuf-lib = %{version}-%{release}
Requires: php-protobuf-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

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
%setup -q -n protobuf-3.21.4
cd %{_builddir}/protobuf-3.21.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-protobuf
cp %{_builddir}/protobuf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
cp %{_builddir}/protobuf-%{version}/third_party/utf8_range/LICENSE %{buildroot}/usr/share/package-licenses/php-protobuf/0e34dfdd1bf9f8645ca4a62f06667167aee0d872
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/protobuf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-protobuf/0e34dfdd1bf9f8645ca4a62f06667167aee0d872
/usr/share/package-licenses/php-protobuf/1b5a14d06dd784e88dadc5c68344be2dc13875b6
