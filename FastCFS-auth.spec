%define FastCFSAuthClient    FastCFS-auth-client
%define FastCFSAuthDevel     FastCFS-auth-devel
%define FastCFSAuthDebuginfo FastCFS-auth-debuginfo
%define FastCFSAuthConfig    FastCFS-auth-config
%define CommitVersion %(echo $COMMIT_VERSION)

Name: FastCFS-auth
Version: 2.0.0
Release: 1%{?dist}
Summary: the auth client library and config files of FastCFS. FastCFS is a high performance cloud native distributed file system for databases, KVM and K8s
License: AGPL v3.0
Group: Arch/Tech
URL:  http://github.com/happyfish100/FastCFS/
Source: http://github.com/happyfish100/FastCFS/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

BuildRequires: libfastcommon-devel >= 1.0.49
BuildRequires: libserverframe-devel >= 1.1.6
Requires: %__cp %__mv %__chmod %__grep %__mkdir %__install %__id
Requires: libfastcommon >= 1.0.49
Requires: libserverframe >= 1.1.6

%description
the auth client library and config files of FastCFS.
FastCFS is a high performance distributed file system which can be used as the back-end storage of databases and cloud platforms.
commit version: %{CommitVersion}

%package -n %{FastCFSAuthDevel}
Requires: %{FastCFSAuthClient} = %{version}-%{release}
Summary: header files of FastCFS auth client

%package -n %{FastCFSAuthClient}
Requires: libfastcommon >= 1.0.49
Requires: libserverframe >= 1.1.6
Summary: FastCFS auth client

%package -n %{FastCFSAuthConfig}
Summary: FastCFS auth config files for sample

%description -n %{FastCFSAuthDevel}
This package provides the header files of libfcfsauthclient
commit version: %{CommitVersion}

%description -n %{FastCFSAuthClient}
FastCFS auth client
commit version: %{CommitVersion}

%description -n %{FastCFSAuthConfig}
FastCFS auth config files for sample
commit version: %{CommitVersion}


%prep
%setup -q

%build
./make.sh --moudlue=auth_client clean && ./make.sh --moudlue=auth_client

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT ./make.sh --moudlue=auth_client install
AUTH_CONFDIR=%{buildroot}/etc/fastcfs/auth/
mkdir -p $AUTH_CONFDIR
cp -R src/auth/conf/* $AUTH_CONFDIR

%post

%preun

%postun

%clean
rm -rf %{buildroot}

%files

%files -n %{FastCFSAuthClient}
/usr/lib64/libfcfsauthclient.so*
/usr/bin/fcfs_user
/usr/bin/fcfs_pool

%files -n %{FastCFSAuthDevel}
%defattr(-,root,root,-)
/usr/include/fastcfs/auth/*

%files -n %{FastCFSAuthConfig}
%defattr(-,root,root,-)
%config(noreplace) /etc/fastcfs/auth/*.conf
%config(noreplace) /etc/fastcfs/auth/keys/*

%changelog
* Thu Apr 22 2021 YuQing <384681@qq.com>
- first RPM release (1.0)
