# $NetBSD$

DISTNAME=	asdf-4.3.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/asdf/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/asdf-format/asdf
COMMENT=	Advanced Scientific Data Format
LICENSE=	modified-bsd

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=6.2:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-jmespath>=0.6.2:../../textproc/py-jmespath
DEPENDS+=	${PYPKGPREFIX}-jsonschema>=3.0.2:../../textproc/py-jsonschema
DEPENDS+=	${PYPKGPREFIX}-lz4>=0.10:../../archivers/py-lz4
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.10.0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-packaging>=16.0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-semantic_version>=2.8:../../devel/py-semantic_version
DEPENDS+=	${PYPKGPREFIX}-yaml>=3.10:../../textproc/py-yaml

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 # py-numpy

USE_PKG_RESOURCES=	yes

.include "../../lang/python/pyversion.mk"
.if ${_PYTHON_VERSION} < 39
DEPENDS+=	${PYPKGPREFIX}-importlib-resources>=3:../../devel/py-importlib-resources
.endif

REPLACE_PYTHON+=	asdf-standard/reference_files/generate/generate
REPLACE_PYTHON+=	asdf/extern/RangeHTTPServer.py
REPLACE_PYTHON+=	asdf/_jsonschema/json/bin/jsonschema_suite

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} asdftool asdftool-${PYVERSSUFFIX} || ${TRUE}

.include "../../lang/python/application.mk"
#.include "../../lang/python/egg.mk"
.include "../../lang/python/wheel.mk"
#.include "../../lang/python/extension.mk"
.include "../../mk/bsd.pkg.mk"
