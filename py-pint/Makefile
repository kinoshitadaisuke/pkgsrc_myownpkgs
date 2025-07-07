# $NetBSD$

DISTNAME=	pint-0.24.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=P/Pint/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/hgrecco/pint/
COMMENT=	Operate and manipulate physical quantities in Python
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 38 39

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=3.4.3:../../devel/py-setuptools_scm

DEPENDS+=	${PYPKGPREFIX}-cramjam>=2.8.3:../../archivers/py-cramjam
DEPENDS+=	${PYPKGPREFIX}-appdirs>=1.4.4:../../devel/py-appdirs
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-babel>=2.8:../../devel/py-babel
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.23:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=3.1.6:../../math/py-uncertainties
DEPENDS+=	${PYPKGPREFIX}-xarray>=0:../../math/py-xarray

# pkgsrc_myownpkgs
DEPENDS+=	flatbuffers>=0:../../pkgsrc_myownpkgs/flatbuffers
DEPENDS+=	${PYPKGPREFIX}-dask>=0:../../wip/py-dask
DEPENDS+=	${PYPKGPREFIX}-mip>=1.13:../../pkgsrc_myownpkgs/py-mip
DEPENDS+=	${PYPKGPREFIX}-flexcache>=0.3:../../pkgsrc_myownpkgs/py-flexcache
DEPENDS+=	${PYPKGPREFIX}-flexparser>=0.3:../../pkgsrc_myownpkgs/py-flexparser

# wip
DEPENDS+=	apache-arrow>=0:../../wip/apache-arrow

post-install:
	cd ${DESTDIR}${PREFIX}/bin && ${MV} pint-convert pint-convert-${PYVERSSUFFIX}

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
