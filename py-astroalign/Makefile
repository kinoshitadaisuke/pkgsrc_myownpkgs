# $NetBSD$

DISTNAME=	astroalign-2.4.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astroalign/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astroalign/
COMMENT=	Python module for aligning astronomical images
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.11:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.15:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-sep>=0:../../pkgsrc_myownpkgs/py-sep

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
