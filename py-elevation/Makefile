# $NetBSD$

DISTNAME=	elevation-1.1.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=e/elevation/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://elevation.bopen.eu
COMMENT=	Downloading global terrain digital elevation models
LICENSE=	apache-2.0

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=42:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=3.4:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm_git_archive>=0:../../pkgsrc_myownpkgs/py-setuptools_scm_git_archive

DEPENDS+=	${PYPKGPREFIX}-appdirs>=0:../../devel/py-appdirs
DEPENDS+=	${PYPKGPREFIX}-click>=0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-fasteners>=0:../../devel/py-fasteners
DEPENDS+=	gmake>=0:../../devel/gmake
DEPENDS+=	curl>=0:../../www/curl
DEPENDS+=	unzip>=0:../../archivers/unzip
DEPENDS+=	gzip>=0:../../archivers/gzip
DEPENDS+=	gdal-lib>=0:../../geography/gdal-lib

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
