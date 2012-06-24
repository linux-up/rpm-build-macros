%define		rpm_macros_rev 1.387
Summary:	PLD Linux RPM build macros
Summary(pl):	Makra do budowania pakiet�w RPM dla Linuksa PLD
Name:		rpm-build-macros
Version:	%{rpm_macros_rev}
Release:	1
License:	GPL
Group:		Development/Building
Source0:	rpm.macros
Source1:	service_generator.sh
Source2:	rpm-build.sh
Patch0:		rpm-build-kernel.patch
Requires:	findutils >= 1:4.2.26
Provides:	rpmbuild(macros) = %{rpm_macros_rev}
Obsoletes:	rpm-macros
Conflicts:	gettext-devel < 0.11
# for _x_libraries macro
Conflicts:	rpm < 4.4.2-27.1
# php-config --sysconfdir
Conflicts:	php-devel < 4:5.2.0-3
Conflicts:	php4-devel < 3:4.4.4-10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir %{_prefix}/lib/rpm

%description
This package contains rpm build macros for PLD Linux.

%description -l pl
Ten pakiet zawiera makra rpm-a do budowania pakiet�w dla Linuksa PLD.

%prep
%setup -qcT
cp %{SOURCE0} rpm.macros
rev=$(awk '/^#.*Revision:.*Date/{print $3}' rpm.macros)
if [ "$rev" != "%rpm_macros_rev" ]; then
	: Update rpm_macros_rev define to $rev, and retry
	exit 1
fi
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_rpmlibdir},/etc/shrc.d}
cp rpm.macros $RPM_BUILD_ROOT%{_rpmlibdir}/macros.build
install %{SOURCE1} $RPM_BUILD_ROOT%{_rpmlibdir}/service_generator.sh
install %{SOURCE2} $RPM_BUILD_ROOT/etc/shrc.d/rpm-build.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_rpmlibdir}/macros.build
%attr(755,root,root) %{_rpmlibdir}/service_generator.sh
/etc/shrc.d/rpm-build.sh
